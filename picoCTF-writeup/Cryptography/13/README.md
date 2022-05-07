* flag = cvpbPGS{abg_gbb_onq_bs_n_ceboyrz}
### Solution
---
1. rot13.com
2. python, c++, ...code
* python
```python
	def rot13(sentence):
    		return ''.join([chr((ord(letter) - 97 + 13) % 26 + 97)
                        		if 97 <= ord(letter) <= 122
                        		else letter
                    		for letter in sentence.lower()])


	if __name__ == '__main__':
    	text = input('Input :')
    	print(rot13(text))



```
