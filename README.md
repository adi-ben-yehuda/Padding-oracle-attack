# Padding oracle attack

## Introduction
In this project, a script that realizes the padding oracle attack is presented.

## Table of contents
* [General Information](#general-information)
* [Contact](#Contact)

## General Information
First, we import the DES library from Cryptodome.Cipher to perform encryption using the DES block cipher. Additionally, we import the pad and unpad library from Cryptodome.Util.Padding to perform padding and unpadding.

Next, we pad the hello world string to be 16 bytes long and it looks like this:

![image](https://github.com/adi-ben-yehuda/security1/assets/75027826/5bb43860-a229-48f1-8b60-b523d15ea4ef)

We flood DES in CBC mode the padded string with the "poaisfun" key and an IV that is all zeros. After encryption, the ciphertext looks like this:

![image](https://github.com/adi-ben-yehuda/security1/assets/75027826/ac6f9674-2116-45a6-8656-e0348734cc0a)

The oracle function receives ciphertext, key, and iv, performs decryption, and removes the padding. If the operation was successful - it returns True, otherwise False.

Now we want to decrypt the ciphertext by finding out all the letters in a block, and then do this for each block in the ciphertext.
We will execute a loop for the number of blocks, which will decode each block until finally the plaintext is decoded. We will notice that in each iteration on a block, we will define c to be a chain of the block of zeros with the eight bytes corresponding to the current block number from the ciphertext.
Now, we will create an inner loop to discover all the bytes of the current block, which will decode one byte until the entire block is decoded.
In the inner loop, we will perform all the steps to decode a single byte using the following formula:

![image](https://github.com/adi-ben-yehuda/security1/assets/75027826/3cc08240-d724-428d-a42f-5da5ab857fe9)

That is, first of all, we will find in the loop the change in c that will return True from the oracle. Then, by the above formula, we will perform xor with the appropriate variables according to i and k.
We will distinguish between the two cases: when k is 0, that is, when it is the first block, we will perform the xor with the IV, but when it is any other block, we will want to perform the xor with the previous block (which we have already found). Finally, we will concatenate the byte x we found to the current block.
Then we will write another loop, the purpose of which is to change c in such a way that the oracle will return True for the next byte, and this with the help of the bytes we have found so far.

In this way, we will turn all the bytes into a value that causes Oracle to return true, that is, by doing so, we discover the next byte in the current block.
Finally we will update c with the changes we found.
At the end of decoding the block (at the end of each iteration of the outer loop) we will update our decoding and concatenate the decoded block to it.
After concatenating all the decoded blocks to our variable, we will remove the padding from it and get the desired result.

## Contact
Created by @adi-ben-yehuda and @shiragolds1 - feel free to contact us!


