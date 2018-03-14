"""[summary]

Bugs:
    计算精度问题
"""
import math
import cmath


class FFT(object):
    """docstring for FFT."""

    def __init__(self, serial):
        super(FFT, self).__init__()
        # Input serial & serial's length
        self.serial = serial
        self.length = int(math.ceil(math.log(len(self.serial)) / math.log(2)))
        # Calculate rotation factor
        self.rotation_factor = [
            cmath.exp(-1 * 2j * cmath.pi * i / 2**self.length)
            for i in range(2**self.length)
        ]
        # Reverse index
        self.reverseIndex()
        # Calculate DFT
        self.result = self.DFT()

    def reverseIndex(self):
        # Format binary and reverse
        reversedIndex = [
            int(bin(i)[2:].zfill(self.length)[::-1], base=2)
            for i in range(2**self.length)
        ]
        # Mapping into original serial
        self.serial = [self.serial[index] for index in reversedIndex]

    def butterfly(self, subSerial):
        half = len(subSerial) // 2
        # Add rotation factor's influence
        for latterIndex in range(half):
            subSerial[half + latterIndex] *= self.rotation_factor[::(
                2**self.length // (2 * half))][latterIndex]
        former, latter = [], []
        # Calculate each value
        for (f, l) in zip(subSerial[:half], subSerial[half:]):
            former.append(f + l)
            latter.append(f - l)
        return former + latter

    def DFT(self):
        serial = self.serial[:]
        for i in range(1, self.length + 1):
            ret = []
            for j in range(2**(self.length - i)):
                ret += self.butterfly(serial[j * 2**i:(j + 1) * 2**i])
            serial = ret
        return serial


class Solution:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        # Preprocess
        length = max(len(num1), len(num2))
        self.length = int(math.ceil(math.log(2 * length) / math.log(2)))
        # Calculate FFT
        fft1 = FFT(self.modifySerial(num1)).result
        fft2 = FFT(self.modifySerial(num2)).result
        # Mulitiply
        fft = [i * j for (i, j) in zip(fft1, fft2)]
        # Calculate IFFT
        # Conjugate
        ifft = [i.conjugate() for i in fft]
        # FFT
        ifft = FFT(ifft).result
        # Normalize
        length = len(ifft)
        ifft = [i / length for i in ifft]
        # Conjugate
        ifft = [i.conjugate() for i in ifft]
        # Postprocess
        ret = 0
        for digit in range(len(ifft)):
            ret += ifft[digit].real * 10**(-1 * digit)
        return str(int(ret * 10**(len(num1) + len(num2) - 2)))

    def modifySerial(self, serial):
        serial = [int(i) for i in serial]
        # Fill zero at the end of sequence
        serial = serial + [0] * (2**self.length - len(serial))
        return serial


if __name__ == "__main__":
    s = Solution()
    output = s.multiply("0", "0")
    print(output)
