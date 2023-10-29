# Padding oracle attack

## Introduction
In this project, a script that realizes the padding oracle attack is presented.

## Table of contents
* [General Information](#general-information)
* [Installation](#installation)
* [Contact](#Contact)

## General Information
First, we import the DES library from Cryptodome.Cipher to perform encryption using the DES block cipher. Additionally, we import the pad and unpad library from Cryptodome.Util.Padding to perform padding and unpadding.
Next, we pad the hello world string to be 16 bytes long and it looks like this:

![image](https://github.com/adi-ben-yehuda/security1/assets/75027826/5bb43860-a229-48f1-8b60-b523d15ea4ef)

We flood DES in CBC mode the padded string with the "poaisfun" key and an IV that is all zeros. After encryption, the ciphertext looks like this:

![image](https://github.com/adi-ben-yehuda/security1/assets/75027826/ac6f9674-2116-45a6-8656-e0348734cc0a)

The oracle function receives ciphertext, key, and iv, performs decryption, and removes the padding. If the operation was successful - it returns True, otherwise False.
We define a variable called c which is a concatenation of a reset block and the second block of the ciphertext. We send this variable to the oracle function in a loop so that each time we increase the eighth byte by one until it returns True.


## Installation
Before installing this project, you need to install on your computer:
* Git
* Node.js
* React
* MongoDB

Then open a terminal.
write the next command:
```
npm i react-router-dom
npx create-react-app yourAppName
```

## Contact
Created by @adi-ben-yehuda and @shiragolds1 - feel free to contact us!


