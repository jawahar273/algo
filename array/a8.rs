// Topic: find Largest sum contiguous Subarray 

#[derive(PartialEq, PartialOrd)]
struct Array { elements: Vec<i64> }

impl Array {

    fn max_value(&self, first: i64, second: i64) -> i64 {
        if first > second {
            return first;
        } else if second > first {
            return second;
        } else {
            return first;
        }
    }

    fn sub_max(&self) -> i64 {
        let mut max = self.elements[0];
        let mut max_till_now = self.elements[0];

        for element in self.elements[1..].iter() {
            let element = *element;
            max_till_now = self.max_value(element, max_till_now + element);
            max = self.max_value(max_till_now, max);
        }
        return max;
    }
}

fn main() {
    let array = Array { elements: vec![-2, 1, -3, 4, -1, 2, 1, -5, 4]  };
    println!("{:?}", array.sub_max());
}
