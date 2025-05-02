# Demo: Robust real-time bandwidth extension for headsets with a microphone conversion target

This is the official demo page of the paper **Robust real-time bandwidth extension for headsets with a microphone conversion target** currently under peer review process.

[[Demo page](#)] [[Paper](#)] [[Dataset](#)]


# Abstract

Headsets are widely used in video conferences and online events, offering a compact solution of headphones, a microphone, and an analog-to-digital (ADC) converter in a single product. However, their microphones often have lower perceptual audio quality than studio microphones: The typically smaller diaphragm sizes are unable to faithfully capture the lower frequency range of human speech and their ADC converters are oftentimes limited to 16kHz (also known as wideband) or lower sample rates. This limitation is particularly prevalent in Bluetooth headsets using Hands-Free Profile (HFP) or Headset Profile (HSP). Artificially extending the input's bandwidth can improve perceptual audio quality; however, in practical applications, reverberation and background noise can significantly degrade the performance of bandwidth extension algorithms.  Furthermore, the maximum achievable quality in the extended bandwidth is limited by the source characteristics.

We propose a multitasking neural network for speech enhancement that effectively reduces noise and reverberation of a wideband input while generating a clean, full-band audio output (48kHz).  Differently from previous approaches, our solution leverages anechoic studio microphone recordings to produce a high quality target, thus, allowing simultaneous reconstruction and enhancement of both low frequencies differences due to diaphragm size limitations as well as high frequencies due to ADC constraints. Our network is designed to operate in real-time and low-complexity setups, allowing it to run on consumer laptops using CPU only or to be deployed on-device for hardware solutions. Model code and dataset recordings are freely available to encourage further research.


# Cite

This section will be updated once the paper is published.


# Acknowledgement

The calculations presented in this publication were carried out using the computer resources of the Aalto University of Science “Science-IT” project.
