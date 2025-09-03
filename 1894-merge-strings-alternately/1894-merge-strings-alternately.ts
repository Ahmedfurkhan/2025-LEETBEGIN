function mergeAlternately(word1: string, word2: string): string {
let merge: string = '';
let i:number = 0,j:number = 0;
while (i<word1.length || j<word2.length){
    if (i<word1.length){
        merge += word1[i++];
    }
    if (j<word2.length){
        merge += word2[j++];
    }
}
return merge;
};