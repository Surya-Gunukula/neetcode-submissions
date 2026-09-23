class Solution:

    def encode(self, strs: List[str]) -> str:
        output_str = ""
        for input_str in strs:
            output_str = output_str + input_str + str(len(input_str)) + "." 
        
        return output_str
    def decode(self, s: str) -> List[str]:
        output_list = []
        i = 1
        while(i < len(s)):
            j = 0
            while(s[i] == "." and s[i-1-j:i].isdigit()):
                str_length = int(s[i-1-j:i])
                print(str_length)
                if(s[i - 2 - j - str_length] == "."):
                    output_list.append(s[i- 1-str_length-j:i-1-j])
                    break;
                else:
                    j += 1
            i += 1
        return output_list
                


