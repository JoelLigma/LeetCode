"""
271. Encode and Decode Strings

Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

Machine 1 (sender) has the function:

string encode(vector<string> strs) {
  // ... your code
  return encoded_string;
}
Machine 2 (receiver) has the function:
vector<string> decode(string s) {
  //... your code
  return strs;
}
So Machine 1 does:

string encoded_string = encode(strs);
and Machine 2 does:

vector<string> strs2 = decode(encoded_string);
strs2 in Machine 2 should be the same as strs in Machine 1.

Implement the encode and decode methods.

You are not allowed to solve the problem using any serialize methods (such as eval).

 

Example 1:

Input: dummy_input = ["Hello","World"]
Output: ["Hello","World"]
Explanation:
Machine 1:
Codec encoder = new Codec();
String msg = encoder.encode(strs);
Machine 1 ---msg---> Machine 2

Machine 2:
Codec decoder = new Codec();
String[] strs = decoder.decode(msg);
Example 2:

Input: dummy_input = [""]
Output: [""]
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] contains any possible characters out of 256 valid ASCII characters.
"""


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))

class Codec:
    def encode(self, strs: List[str]) -> str:
        """
        Encodes a list of strings to a single string.
        """
        # To solve this problem we use a concept called escaping.
        # First, we choose a delimiter to seperate each str in the list: <;
        # If we come across a < in any string we simply add another < to it (escaping it)

        encoded_str = ""
        for s in strs:
            temp = ""
            for ch in s:
                temp += ch + "<" if ch == "<" else ch
            temp += "<;"
            encoded_str += temp
        return encoded_str

        

    def decode(self, s: str) -> List[str]:
        """
        Decodes a single string to a list of strings.
        """
        decoded = []
        temp = ""
        i = 0
        while i < len(s):
            if s[i:i+2] == "<;":
                decoded += [temp]
                temp = ""
                i += 2
            elif s[i:i+2] == "<<":
                temp += "<"
                i += 2
            else:
                temp += s[i]
                i += 1
        return decoded

# Time complexity: O(n), because both the en- and de-coding process iterates over each character once
# Space complexity: O(k), because we use space for each escape characters and delimiter 
