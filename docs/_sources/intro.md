# Introduction

**Biomedical Signal Processing**

**From Fundamentals to Advanced Methods, with Python**

*Kim Nguyen*

---

## About me and this book

I am Kim Nguyen, a master's student in Smart Medicine and Health Informatics at National Taiwan University. My background is in International Business, and I began learning data science and machine learning independently before moving into health informatics. That path shapes how I want to explain this subject: I want the connection between an idea, its equation, and its code to be visible, with enough intermediate steps to follow the reasoning.

My thesis focuses on the ECG, so it is the signal I return to throughout this book. Before using a recording in an analysis, I want to understand what the electrodes measured, where noise comes from, and how each processing choice changes the waveform. A smoother trace is only the beginning; changes in amplitude, shape, and timing matter too.

We will begin with signals and simple calculations, then work toward Fourier analysis, filtering, ECG preprocessing, and more advanced methods. I use **I** for my perspective and choices, and **we** when working through an example together. Other physiological signals help us see which ideas transfer and which depend on the measurement.

I am developing this book as part of my preparation for further research and PhD study. I want it to document how I reason about biomedical signals and offer a useful learning resource for others, including those approaching the subject from a different field. My [portfolio](https://kimnguyen2002.github.io/Portfolio/) includes my wider work in healthcare and data science, and my code is available on [GitHub](https://github.com/kimnguyen2002).

## Acknowledgments

My interest in this subject grew through the *Biomedical Signal Processing* class taught by [Professor Wen-Chau Wu](https://scholars.lib.ntu.edu.tw/entities/person/77283ea3-91d6-4cd9-a161-5d87d940a90e) at National Taiwan University. The class encouraged me to look more closely at the ideas behind the equations and to continue studying biomedical signals beyond the course.

I am also deeply grateful to my advisor, [Fei-Man Hsu](https://scholars.lib.ntu.edu.tw/entities/person/8d6890f0-782a-4eaa-83f6-63034e162d60), for supporting my work and encouraging me to follow my interests. That encouragement has helped me keep learning and develop this project alongside my research.

## Sources behind these notes

These notes draw on published books in signal processing, biomedical measurement, and ECG analysis. The explanations and Python examples are my way of working through those ideas; the underlying theory belongs to the wider literature. The [books and references](bibliography.md) page lists the main textbooks, and citations within the chapters identify further sources for particular methods and datasets.

## Scope of this edition

This edition brings together the existing lessons on biomedical signals, mathematical foundations, systems, Fourier analysis, sampling, filters, and physiological applications. Chapters, sections, and equations are numbered consecutively within this edition.

## Who this book is for

The book is written for students and researchers in biomedical engineering, health informatics, medicine, physiology and data science who want a solid working understanding of signal processing. I assume you are comfortable with high-school algebra and trigonometry and have seen a little calculus. The mathematical toolkit in Chapter 2 introduces complex numbers and Euler’s formula. In the available sections, I explain the notation as it appears. Some familiarity with Python helps; [Appendix A](appendix/a_python_essentials.ipynb) covers the essentials that the code relies on.

If you already know signal processing, you can use the ECG examples as a starting point and return to the foundations when needed. If the mathematics is new to you, work through a small example before trying to follow a full derivation. It is fine to pause at a symbol and check what it means.

## How the book is organized

The sidebar groups the lessons by subject, from foundations and systems to frequency analysis, filtering, and physiological signals. Each chapter page lists the lessons included in this edition. The ECG remains the main running example, with EEG and wavelet analysis providing further applications.

The appendices provide practical references for Python, datasets, formulas, terminology, data types, pandas, NumPy, LaTeX, and mathematical symbols. You can return to them whenever a calculation or a piece of notation needs clarification.

## How I suggest reading the equations

An equation is a compact description of an operation. Before following a derivation, identify the input, the output, and the units. Then try one small numerical example. Once that example makes sense, the general notation is easier to follow.

For example, a three-sample moving average is

$$
y[n] = \frac{x[n] + x[n-1] + x[n-2]}{3}.
$$

Here, $x$ is the input recording, $y$ is the smoothed output, and $n$ is the sample index. At a particular index, we take the current sample and the two preceding samples, add them, and divide by three. If those values are $0.3$, $0.6$, and $0.9$ mV, the result is $0.6$ mV. We repeat the same operation at the next index to obtain the next output sample. The output still has units of millivolts.

This also gives us a question to ask of the figure: did the averaging reduce unwanted fluctuations, and did it flatten a peak we wanted to preserve? I use that connection between the calculation and the waveform throughout the book.

## How to read and run the notebooks

The worked teaching sections are Jupyter notebooks with saved code outputs and figures. You can read them without running the code, or open them locally and work through the cells in order. When using an online notebook service, make sure the example data and plotting style are available at the paths used in the notebook. To run everything locally:

```bash
git clone https://github.com/kimnguyen2002/biomedical-signal-processing.git
cd biomedical-signal-processing
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
jupyter lab book/
```

The recordings used in the book are stored in the `book/data/` folder of the repository and described in [Appendix B](appendix/b_datasets.ipynb). All of them come from [PhysioNet](https://physionet.org) {cite:p}`goldberger2000`.

## Quick references

The appendices are there to return to while reading, rather than prerequisites to memorize.

| If you need help with… | Start here |
|---|---|
| Python values, types, and missing data | [Data types](appendix/e_data_types.ipynb) |
| Annotation tables and CSV files | [pandas](appendix/f_pandas.ipynb) |
| Arrays, indexing, shapes, and arithmetic | [NumPy](appendix/g_numpy.ipynb) |
| Writing equations in a notebook | [LaTeX](appendix/h_latex.ipynb) |
| Reading a mathematical symbol | [Symbols and notation](appendix/i_math_symbols.ipynb) |
| Looking up an identity or transform | [Mathematical reference](appendix/c_math_reference.ipynb) |
| Understanding a technical term | [Glossary](appendix/d_glossary.md) |
| Finding the example recordings | [Datasets](appendix/b_datasets.ipynb) |

## Conventions

Mathematics is typeset with the engineering convention $j = \sqrt{-1}$. Continuous-time signals are written $x(t)$ and discrete-time signals $x[n]$. Frequencies in hertz are written $f$, continuous-time angular frequencies $\omega = 2\pi f$, and discrete-time angular frequencies $\Omega = 2\pi f / f_s$. The full notation table is in [Appendix C](appendix/c_math_reference.ipynb). Physiological quantities carry their usual units: millivolts for the ECG, microvolts for the EEG, hertz for frequency and seconds or milliseconds for time.

Code cells that only draw figures are collapsed on the website; click on them to see the code. Cells that implement an algorithm are always shown.

## Feedback and citation

Corrections and suggestions are very welcome. Please open an issue on the [GitHub repository](https://github.com/kimnguyen2002/biomedical-signal-processing/issues).

If you find the book useful in your work, you can cite it as:

```bibtex
@book{nguyen2026bsp,
  author    = {Nguyen, Kim},
  title     = {Biomedical Signal Processing: From Fundamentals to Advanced Methods, with Python},
  year      = {2026},
  url       = {https://kimnguyen2002.github.io/biomedical-signal-processing/}
}
```

The text is licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) and the code under the [MIT License](https://opensource.org/licenses/MIT).
