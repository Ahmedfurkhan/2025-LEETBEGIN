class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        string merge;
        int i=0,j=0;
        int len1 = word1.length();
        int len2 = word2.length();

        while (i<len1 || j<len2){
            if (i<len1){
                merge += word1[i++];
            }
            if (j<len2){
                merge += word2[j++];
            }
        }
        return merge;                
    }
};