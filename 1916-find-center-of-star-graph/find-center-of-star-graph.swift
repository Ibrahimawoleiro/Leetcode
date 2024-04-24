class Solution {
    func findCenter(_ edges: [[Int]]) -> Int {
        
        var a = edges[0][0];
        var b = edges[0][1];
        var c = edges[1][0];
        var d = edges[1][1];

        if a == b{
            return a;
        }else if a == c{
            return a;
        }else if a == d {
            return a;
        }

        if b == a{
            return b;
        }else if b == c{
            return b;
        }else if b == d {
            return b;
        }

        if c == a{
            return c;
        }else if c == b{
            return c;
        }else if c == d {
            return c;
        }

        if d == a{
            return d;
        }else if d == b{
            return d;
        }else if d == c {
            return d;
        }
        return 0;
    }
}