
<!-- TABLE OF CONTENTS -->

## Table of contents
* [Digital Signal Processor (DSP) Architecture](#Digital-Signal-Processor-(DSP)-Architecture)
* [Technology stack](#Technology-stack)
* [Laboratories 1 - warm-up](#Laboratories1-warm-up)
* [Laboratories 2 - ADC](#Laboratories2-ADC)
* [Laboratories 3 - DAC](#Laboratories3-DAC-warm-up)
* [Laboratories 4 - Modulations](#Laboratories4-Modulations)
* [Laboratories 5 - Filters](#Laboratories5-warmFilters)
* [Laboratories 6 - Heartbeat signal processing](#Laboratories6-Heartbeat-signal-processing)
* [Laboratories 7 - OpenCV face and cars' license plates detection](#Laboratories7-OpenCV-face-and-cars'-license-plates-detection)
* [Laboratories 8 - Perceptron](#Laboratories8-Perceptron)

<!-- <details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#digital-signal-processor-(dsp)-architecture">Digital Signal Processor (DSP) Architecture</a>
      <ul>
        <li><a href="#technology-stack">Technology stack</a></li>
      </ul>
    </li>
    <li><a href="#laboratories-1-warm-up">Laboratories 1 - warm-up</a></li>
    <li><a href="#laboratories-2-adc">Laboratories 2 - ADC</a></li>
    <li><a href="#laboratories-3-dac">Laboratories 3 - DAC</a></li>
    <li><a href="#laboratories-4-modulations">Laboratories 4 - Modulations</a></li>
    <li><a href="#laboratories-5-filters">Laboratories 5 - Filters</a></li>
    <li><a href="#laboratories-6-hearbeat-signal-processing">Laboratories 6 - Heartbeat signal processing</a></li>
    <li><a href="#laboratories-7-opencV-face-and-cars'-license-plates-detection">Laboratories 7 - OpenCV face and cars' license plates detection</a></li>
    <li><a href="#laboratories-8-perceptron">Laboratories 8 - Perceptron</a></li>
  </ol>
</details> -->


<!-- ------------------------------------------------- -->

## Digital Signal Processor (DSP) Architecture

The aim of these classes was to obtain knowledge related to digital signal processing, algorithms permformed on STM32, some computer vision issues and introduction to neural networks.


<p align="right">(<a href="#readme-top">back to top</a>)</p>


### Technology stack

During these classes the following tools have been used:
*   C
*   STM32
*   Python
*   OpenCV
*   TensorFlow


<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- ------------------------------------------------- -->

## Laboratories 1 - warm

The purpose of this classes was to get familiar with STM32CubeIDE and basics of HAL. That's why I will skip the details 


<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ------------------------------------------------- -->

## Laboratories 2 - ADC

During these laboratories I had to measure the sine signal from external device - Analog Discovery 2 of Digilent. Those signal had to be generated with different frequency.

![Alt text](./README_IMG/ADC_1k.png "Title")

Then fast Fourier transform (FFT) had to be perfomed for those signals. The task was to observe the aliasing effect - when the signal's frequency is higher than the half of the sampling freqency


![Alt text](./README_IMG/FFT_ADC_1k.png "Title")
![Alt text](./README_IMG/FFT_ADC_10k.png "Title")

ADC was also performed for simple ADC and through the DMA module. Moreover DMA helped to perform oversampling which resulted in better Effective number of bits (ENOB):

<div id="image-table">
    <table>
        <tr>
            <td>Simple ADC</td>
            <td>ADC with DMA and oversampling</td>
        </tr>
	    <tr>
    	    <td>
                <img src="./README_IMG/FFT_ADC_10k.png"  />
      	    </td>
            <td>
                <img src="./README_IMG/FFT_DMA_10k.png"  /> 
            </td>
        </tr>
    </table>
</div>

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ------------------------------------------------- -->

## Laboratories 3 - DAC

In this exercise there was a need to generate sine wave from look-up table (LUT).

![Alt text](./README_IMG/1kHz.png)

Moreover Direct digital synthesis (DDS) method has been implemented. Thanks to this it was possible to gneerate sine wave with any frequency (of course the higher frequency the more deformated sine wave is). For frequency f=1kHz:

![Alt text](./README_IMG/TIME_1kHz.png)

For frequency f=10kHz:
![Alt text](./README_IMG/TIME_10kHz.png)


<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ------------------------------------------------- -->

## Laboratories 4 - Modulations




<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ------------------------------------------------- -->

## Laboratories 5 - Filters




<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ------------------------------------------------- -->

## Laboratories 6 - Heartbeat signal processing




<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ------------------------------------------------- -->

## Laboratories 7 - OpenCV face and cars' license plates detection




<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ------------------------------------------------- -->

## Laboratories 8 - Perceptron




<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ------------------------------------------------- -->



