# Visual Cryptography

The basic model consists of a printed page of ciphertext and a printed transparency. The original plaintext is revealed by placing the transparency (over) over the printed page (ciphertext), even though each one of them is indistinguishable from white noise.

## (2, N) Sharing Case

Sharing a secret with an arbitrary number of people N such that at least 2 of them are required to decode the secret.

Every pixel from the secret image is encoded into multiple subpixels in each share image using a matrix to determine the color of the pixels. In the (2,N) case a white pixel in the secret image is encoded using a matrix from the following set, where each row gives the subpixel pattern for one of the components:

<img src="https://raw.githubusercontent.com/mgp25/CTFs/master/2018/ElevenPaths/Visual_Cryptography/P-Matrix.png" width=400>

For instance in the (2,2) sharing case (the secret is split into 2 shares and both shares are required to decode the secret) we use complementary matrices to share a black pixel and identical matrices to share a white pixel. Stacking the shares we have all the subpixels associated with the black pixel now black while 50% of the subpixels associated with the white pixel remain white.

## Example

<img src="https://raw.githubusercontent.com/mgp25/CTFs/master/2018/ElevenPaths/Visual_Cryptography/visual.gif" width=400>

## Libraries

- [ageron/visual_crypto](https://github.com/ageron/visual_crypto)

## References

[1] Moni Naor, Adi Shamir. "Visual Cryptography". 1995. Available in: [http://www.fe.infn.it/u/filimanto/scienza/webkrypto/visualdecryption.pdf](http://www.fe.infn.it/u/filimanto/scienza/webkrypto/visualdecryption.pdf)

[2] Visual Cryptography. Available in: [https://en.wikipedia.org/wiki/Visual_cryptography](https://en.wikipedia.org/wiki/Visual_cryptography)

