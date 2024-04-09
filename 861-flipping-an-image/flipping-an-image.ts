function flipAndInvertImage(image: number[][]): number[][] {
    for(let i = 0; i < image.length; i++){
        let j: number = 0;
        let k: number = image[0].length - 1;
        while(j <= k){
            let left: number = image[i][j];
            let right: number = image[i][k];
            console.log(`left${left}   right${right}`)
            let temp: number = left;
            left = right;
            right = temp;
            if(left == 1){
                image[i][j] = 0;
            }else{
                image[i][j] = 1;
            }
            if(right == 1){
                image[i][k] = 0;
            }else{
                image[i][k] = 1;
            }
            j++;
            k--;
            console.log(i)
        }
    }
            return image;
};