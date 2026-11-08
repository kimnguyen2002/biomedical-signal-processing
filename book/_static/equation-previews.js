(() => {
 function init() {
  "use strict";
  const data = window.BSP_EQUATION_PREVIEWS || {};
  const keys = Object.keys(data);
  const panel = document.createElement("div");
  panel.id = "equation-preview";
  panel.className = "equation-preview";
  panel.role = "tooltip";
  panel.hidden = true;
  document.body.append(panel);
  let active = null, version = 0, openTimer, closeTimer;

  function entry(link) {
    const url = new URL(link.href, location.href);
    if (url.origin !== location.origin) return null;
    const key = keys.find(key => decodeURIComponent(url.pathname).endsWith("/" + key.split("#")[0]) && url.hash === "#" + key.split("#")[1]);
    return key ? data[key] : null;
  }
  function hide() {
    clearTimeout(openTimer);
    clearTimeout(closeTimer);
    version++;
    if (active) active.removeAttribute("aria-describedby");
    active = null;
    panel.hidden = true;
  }
  function area(a, b) {
    return Math.max(0, Math.min(a.right, b.right) - Math.max(a.left, b.left)) * Math.max(0, Math.min(a.bottom, b.bottom) - Math.max(a.top, b.top));
  }
  function place(link) {
    const ref = link.getBoundingClientRect();
    const width = panel.offsetWidth, height = panel.offsetHeight, gap = 10, margin = 12;
    const center = ref.left + ref.width / 2;
    // Only consider positions adjacent to the reference; never jump to a page corner.
    const obstacles = [];
    document.querySelectorAll(".bd-article .math:not(span)").forEach(node => {
      const r = node.getBoundingClientRect();
      if (r.bottom > 0 && r.top < innerHeight && Math.abs((r.top + r.bottom) / 2 - ref.top) < 300) obstacles.push(r);
    });
    const candidates = [
      [center - width / 2, ref.top - height - gap],
      [center - width / 2, ref.bottom + gap],
      [ref.right + gap, ref.top + ref.height / 2 - height / 2],
      [ref.left - width - gap, ref.top + ref.height / 2 - height / 2],
      [ref.left, ref.top - height - gap],
      [ref.left, ref.bottom + gap]
    ].map(([x, y]) => {
      x = Math.max(margin, Math.min(x, innerWidth - width - margin));
      y = Math.max(margin, Math.min(y, innerHeight - height - margin));
      const box = {left:x, top:y, right:x + width, bottom:y + height};
      const overlap = area(box, ref) * 10000 + obstacles.reduce((sum, r) => sum + area(box, r), 0);
      const dx = Math.max(ref.left - box.right, box.left - ref.right, 0);
      const dy = Math.max(ref.top - box.bottom, box.top - ref.bottom, 0);
      return {x, y, score:overlap + Math.hypot(dx, dy) * 20};
    });
    candidates.sort((a, b) => a.score - b.score);
    panel.style.left = `${candidates[0].x}px`;
    panel.style.top = `${candidates[0].y}px`;
  }
  async function show(link) {
    const preview = entry(link);
    if (!preview) return;
    clearTimeout(closeTimer);
    if (active === link && !panel.hidden) return;
    hide();
    active = link;
    const ticket = version;
    try {
      await window.MathJax?.startup?.promise;
      if (!window.MathJax?.tex2chtmlPromise) return hide();
      const rendered = await MathJax.tex2chtmlPromise(preview.tex, {display:true});
      if (ticket !== version || active !== link) return;
      // A tooltip never duplicates equation anchors in the document.
      rendered.removeAttribute("id");
      rendered.querySelectorAll("[id]").forEach(node => node.removeAttribute("id"));
      panel.replaceChildren(rendered);
      panel.hidden = false;
      link.setAttribute("aria-describedby", panel.id);
      place(link);
    } catch (_) {
      if (ticket === version) hide();
    }
  }
  function scheduleClose() {
    clearTimeout(openTimer);
    closeTimer = setTimeout(() => {
      if (!panel.matches(":hover") && !(active && (active.matches(":hover") || document.activeElement === active))) hide();
    }, 180);
  }
  document.querySelectorAll('a[href*="#eq-"], a[href*="#sec-"]').forEach(link => {
    if (!entry(link)) return;
    link.classList.add("has-equation-preview");
    link.addEventListener("mouseenter", () => {
      clearTimeout(closeTimer);
      clearTimeout(openTimer);
      openTimer = setTimeout(() => show(link), 180);
    });
    link.addEventListener("mouseleave", scheduleClose);
    link.addEventListener("focus", () => show(link));
    link.addEventListener("blur", scheduleClose);
    link.addEventListener("click", hide);
  });
  panel.addEventListener("mouseenter", () => clearTimeout(closeTimer));
  panel.addEventListener("mouseleave", scheduleClose);
  document.addEventListener("keydown", event => { if (event.key === "Escape") hide(); });
  window.addEventListener("scroll", hide, {passive:true});
  window.addEventListener("resize", hide, {passive:true});
 }
 if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init, {once:true});
 else init();
})();
