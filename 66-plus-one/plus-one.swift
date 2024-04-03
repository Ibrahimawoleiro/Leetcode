class Solution {
    func plusOne(_ digits: [Int]) -> [Int] {
        // //1
        // var ans = 0
        // var result: [Int] = [Int]()
        // for index in 0..<digits.count{
        //     if index == 0{
        //         ans+=digits[index]
        //         continue
        //     }
        //     ans *= 10
        //     ans += digits[index]
        // }
        // ans += 1
        // while ans > 0{
        //     result.append(ans % 10)
        //     ans = Int(ans / 10)
        // }
        // result.reverse()
        // return result

        //2
        var copiedArray = Array(digits)
        copiedArray.reverse()
        var remainder:Int = 1
        for index in stride(from: 0, to: copiedArray.count, by: 1){
            var sum: Int = remainder + copiedArray[index]
            remainder = 0
            if sum > 9{
                copiedArray[index] = 0
                remainder = 1
            }else{
                copiedArray[index] = sum
            }
        }
        if remainder  == 1{
            copiedArray.append(1)
        }
        copiedArray.reverse()
        return copiedArray
    }
}