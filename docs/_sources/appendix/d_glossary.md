# D. Glossary

This glossary collects the terms that appear most often in the book. Each entry gives a short working definition and, where useful, the section in which the idea is developed.

## A–C

Aliasing
: The folding of frequency components above half the sampling rate into lower frequencies, so that they become indistinguishable from genuine low-frequency content after sampling. See [Section 6.2](../ch09_sampling/index.md).

Analytic signal
: The complex signal $z(t) = x(t) + j\,\mathcal{H}\{x(t)\}$ whose spectrum is zero at negative frequencies. Its magnitude and angle give the instantaneous amplitude and phase. See Section 23.4.

Anti-aliasing filter
: An analog low-pass filter placed before the analog-to-digital converter to remove energy above half the sampling rate. See [Section 11.2](../ch17_ecg/index.md).

Artifact
: Any component of a recording that does not originate from the physiological process of interest, such as electrode motion, muscle activity in an ECG, or eye blinks in an EEG.

Atrial fibrillation (AF)
: An arrhythmia in which disorganized atrial activity replaces the P wave and produces an irregularly irregular ventricular rhythm. See Section 19.4.

Autocorrelation
: The correlation of a signal with a delayed copy of itself, as a function of the delay. Periodic signals have autocorrelation peaks at multiples of their period. See Section 6.1.

Autoregressive (AR) model
: A model in which each sample is a linear combination of past samples plus white noise. It leads to parametric spectral estimates. See [Section 7.4](../ch12_spectral_estimation/index.md).

Band-pass filter
: A filter that passes frequencies between a lower and an upper cutoff and attenuates the rest.

Baseline wander
: A slow drift of the ECG baseline, mostly below 0.5–1 Hz, caused by respiration, movement and changes in electrode–skin impedance. See [Section 12.2](../ch18_ecg_preprocessing/index.md).

Bilinear transform
: The mapping $s = \frac{2}{T_s}\frac{1 - z^{-1}}{1 + z^{-1}}$ used to turn an analog filter into a digital one while preserving stability. See Section 15.2.

BIBO stability
: Bounded-input, bounded-output stability: every bounded input produces a bounded output. An LTI system is BIBO stable if and only if its impulse response is absolutely summable.

Butterworth filter
: A filter whose magnitude response is maximally flat in the passband. See Section 15.1.

Common-mode rejection ratio (CMRR)
: The ratio of a differential amplifier's differential gain to its common-mode gain, usually given in decibels. A high CMRR suppresses interference that appears equally on both electrodes.

Convolution
: The operation $y[n] = \sum_k x[k]\,h[n-k]$ that gives the output of an LTI system from its input and impulse response. See [Section 4.2](../ch05_convolution/02_convolution_sum.ipynb).

Cutoff frequency
: The frequency at which a filter's gain has fallen to a specified level, usually $-3$ dB (half power).

## D–H

Decibel (dB)
: A logarithmic unit for ratios: $10\log_{10}$ of a power ratio or $20\log_{10}$ of an amplitude ratio.

Detrended fluctuation analysis (DFA)
: A method for estimating long-range correlations in a nonstationary time series, widely applied to RR-interval series. See Section 26.3.

Discrete Fourier transform (DFT)
: The transform $X[k] = \sum_{n=0}^{N-1} x[n]\,e^{-j2\pi kn/N}$ of a finite sequence, computed in practice with the FFT. See Section 10.2.

Discrete wavelet transform (DWT)
: A multiresolution decomposition of a signal into approximation and detail coefficients computed with a cascade of filters and downsamplers. See [Section 14.1](../ch24_wavelets/index.md).

Electrocardiogram (ECG)
: The recording of the heart's electrical activity from electrodes on the body surface, typically 0.5–4 mV in amplitude.

Electroencephalogram (EEG)
: The recording of the brain's electrical activity from scalp electrodes, typically a few to about 100 µV.

Electromyogram (EMG)
: The recording of the electrical activity of skeletal muscle, by surface or needle electrodes.

Ergodicity
: The property of a random process whose time averages equal its ensemble averages, which allows statistics to be estimated from a single long recording.

Fast Fourier transform (FFT)
: A family of algorithms that compute the DFT in $O(N\log N)$ operations instead of $O(N^2)$. See Section 10.3.

FIR filter
: A finite impulse response filter, whose output depends only on a finite number of input samples. FIR filters are always stable and can have exactly linear phase.

Frequency response
: The complex gain $H(\omega)$ or $H(e^{j\Omega})$ that an LTI system applies to a sinusoid of each frequency. See Section 8.4.

Gibbs phenomenon
: The persistent overshoot of about 9% of the jump that appears near a discontinuity when a signal is approximated by a truncated Fourier series. See [Section 5.3](../ch07_fourier_series/index.md).

Group delay
: The negative derivative of the phase response, $-d\varphi/d\omega$; the delay experienced by the envelope of a narrowband signal. See [Section 13.2](../ch13_filter_fundamentals/index.md).

Heart rate variability (HRV)
: The beat-to-beat variation of the interval between heartbeats, quantified in the time, frequency and nonlinear domains. See Section 19.2.

High-pass filter
: A filter that attenuates frequencies below a cutoff and passes those above it.

## I–P

IIR filter
: An infinite impulse response filter, implemented recursively with feedback. IIR filters reach sharp responses at low order but generally have nonlinear phase.

Impulse response
: The output of a system when the input is a unit impulse. For an LTI system it characterizes the system completely.

Independent component analysis (ICA)
: A method that recovers statistically independent sources from their linear mixtures by maximizing non-Gaussianity. See Section 25.2.

Isoelectric line
: The flat segment of the ECG, usually taken in the PR segment, that serves as the zero-voltage reference.

Linear phase
: A phase response proportional to frequency, which delays all components equally and therefore preserves waveform shape.

LTI system
: A system that is both linear and time-invariant, fully described by its impulse response.

Median frequency
: The frequency that divides the power spectrum into two halves of equal power, widely used to track muscle fatigue in the EMG.

Motion artifact
: Interference caused by movement of the electrodes or the body. In the ECG it overlaps the QRS frequency band and is hard to filter.

Notch filter
: A narrow band-stop filter that removes a single frequency, such as 50 or 60 Hz power-line interference. See Section 15.4.

Nyquist frequency
: Half the sampling rate, $f_s/2$, the highest frequency that can be represented without aliasing.

Periodogram
: The squared magnitude of the DFT of a signal, scaled to estimate its power spectral density. It is unbiased in the limit but has a high variance. See [Section 7.3](../ch12_spectral_estimation/index.md).

Photoplethysmogram (PPG)
: An optical signal that tracks blood-volume changes in tissue with each heartbeat, measured by pulse oximeters and wearable devices.

Pole and zero
: Values of $z$ (or $s$) at which a transfer function becomes infinite (poles) or zero (zeros). Their positions determine the frequency response and stability.

Power-line interference
: Contamination at the mains frequency (50 or 60 Hz) and its harmonics, coupled into recordings capacitively, magnetically or through ground loops. See [Section 18.4](../ch18_ecg_preprocessing/index.md).

Power spectral density (PSD)
: The distribution of a signal's power over frequency, the Fourier transform of its autocorrelation. See [Section 7.2](../ch12_spectral_estimation/index.md).

PRD
: Percentage root-mean-square difference, a normalized error between a reference and a processed signal, common in ECG denoising and compression studies.

## Q–Z

QRS complex
: The sharp, high-amplitude ECG deflection produced by ventricular depolarization, normally 80–120 ms wide.

QRS detection
: The automatic localization of QRS complexes (R peaks) in an ECG, the first step in most ECG analysis. See Section 19.1.

Quantization
: The rounding of sample values to a finite set of levels in analog-to-digital conversion. See [Section 9.4](../ch09_sampling/index.md).

RR interval
: The time between successive R peaks, the basis of heart rate and HRV measurements.

Sampling theorem
: A band-limited signal with no content at or above $B$ Hz is completely determined by samples taken at a rate $f_s > 2B$. See [Section 6.1](../ch09_sampling/index.md).

Sample entropy
: A measure of the irregularity of a time series: the negative logarithm of the conditional probability that sequences similar for $m$ points remain similar at $m + 1$ points. See Section 26.2.

Signal averaging
: Averaging many time-locked repetitions of a signal to reduce uncorrelated noise; the noise power falls as $1/N$. See [Section 10.1](../ch16_noise_removal/index.md).

Signal quality index (SQI)
: A number that summarizes how usable a segment of a recording is, for example by its kurtosis or by the agreement of two QRS detectors. See [Section 18.5](../ch18_ecg_preprocessing/index.md).

Signal-to-noise ratio (SNR)
: The ratio of signal power to noise power, usually expressed in decibels. See Section 3.4.

Spectral leakage
: The spreading of a sinusoid's energy into neighboring DFT bins when the analysis window does not contain a whole number of periods. See Section 10.4.

Spectrogram
: The squared magnitude of the short-time Fourier transform, displayed as a time–frequency image. See Section 23.2.

Stationarity
: The property of a random process whose statistics do not change with time. Wide-sense stationarity requires only a constant mean and an autocorrelation that depends on the lag alone.

Transfer function
: The ratio $H(z) = Y(z)/X(z)$ (or $H(s)$) that describes an LTI system in the transform domain. See Section 11.3.

Wiener filter
: The linear filter that minimizes the mean-squared error between its output and a desired signal. See [Section 10.2](../ch16_noise_removal/index.md).

Window function
: A taper applied to a finite segment before spectral analysis or used to truncate an ideal filter's impulse response, trading main-lobe width against sidelobe level.

Zero-phase filtering
: Filtering a signal forward and then backward so that phase shifts cancel, which preserves the timing of waveform features. It is noncausal and therefore only possible offline. See Section 15.3.

Z-transform
: The transform $X(z) = \sum_n x[n] z^{-n}$, which generalizes the DTFT and turns difference equations into algebraic equations. See Section 11.1.

## Programming and notebook terms

Array
: An indexed collection of values. A NumPy array has a shape and a dtype; a multichannel recording here uses rows for samples and columns for channels. See [NumPy](g_numpy.ipynb).

Axis
: A dimension of an array. For shape `(samples, channels)`, reducing over `axis=0` combines the sample dimension and returns one result per channel.

Boolean mask
: An array of true/false values used to select positions, such as samples within a chosen time interval.

Broadcasting
: NumPy's rules for combining compatible shapes without explicitly repeating each value. For example, one mean per channel can be subtracted from every sample row.

DataFrame
: A pandas table with labeled rows and columns. Useful for beat annotations, metadata, and extracted features. See [pandas](f_pandas.ipynb).

Data type (dtype)
: The representation of a value. A NumPy dtype also specifies storage details such as numerical width. A dtype does not specify physical units. See [data types](e_data_types.ipynb).

Floating-point number
: A finite-precision representation of a real number. Most decimal fractions are approximated, so arithmetic comparisons may require a suitable tolerance.

Index
: A position or label identifying an item. A sample index becomes a time only after using the sampling rate and a time origin.

Integer overflow
: A result outside the range of a fixed-width integer dtype. Convert raw integer arrays to an appropriate calculation dtype before operations such as squaring.

LaTeX
: A typesetting language whose math commands are used in notebook equations. It describes mathematical notation and does not execute a numerical calculation. See [LaTeX](h_latex.ipynb).

Missing value
: An unavailable or undefined observation, represented by a marker such as `np.nan` or `pd.NA`. A missing measurement is different from a measured zero.

NumPy
: Python's array library used here for numerical waveform calculations. See [NumPy](g_numpy.ipynb).

pandas
: Python's table library used here for labeled metadata, annotation tables, and features. See [pandas](f_pandas.ipynb).

Series
: A one-dimensional labeled pandas data structure, often used as one column of a table.

Shape
: The lengths of an array's dimensions. A shape of `(3600, 2)` means 3,600 rows and two columns; the analyst must still define what those dimensions represent.

Slice
: A selection such as `x[start:stop]`, which includes `start` and excludes `stop`. A basic NumPy slice generally shares memory with its source.

View and copy
: A view shares data storage with another array; a copy owns independent data. Editing a view can change the original recording.

Vectorization
: Expressing operations on whole arrays rather than processing each sample in a Python loop. The result still needs checks for shapes, units, and numerical precision.

For mathematical notation, including sums, integrals, complex conjugation, and frequency symbols, see the [symbol guide](i_math_symbols.ipynb).
