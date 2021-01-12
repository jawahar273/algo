// Topic: Minimise the maximum difference between heights 

use std::cmp::min;

struct Array { elements: Vec<i64> }

impl Array {
    fn get_min_diff(&mut self, k: i64) -> i64 {
        self.elements.sort();
        let len_elems = self.elements.len();
        let ans = self.elements[len_elems - 1] - self.elements[0];
        let mut small = self.elements[0] + k;
        let mut big = self.elements[len_elems - 1] - k;
        if small > big {
            small = big;
            big =small;
        }

        for element in &self.elements[1..] {
            let add = *element + k;
            let sub = *element - k;

            if sub >= small || add >= big {
                continue;
            }

            if big - small <= add - sub {
                small = sub
            } else {
                big = add
            }
        }
        return min(ans, big - small);
    }
}

fn main() {
    let mut array = Array{ elements: vec![3, 9, 12, 16, 20] };
    println!("Min heights: {}", array.get_min_diff(3))
}
