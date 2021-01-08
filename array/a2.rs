
struct MinMaxArray { elements: Vec<i64> }

impl MinMaxArray {
    fn min(&self) -> i64 {
        let mut temp: i64 = self.elements[0];
        for element in &self.elements {
            if temp > *element {
                temp = *element;
            }
        }
        return temp;
    }

    fn max(&self) -> i64 {
        let mut temp = self.elements[0];
        for element in &self.elements {
            if temp < *element {
                temp = *element
            }
        }
        return temp;
    }
}


fn main() {

    let min_max_el = MinMaxArray{  elements: vec![1, 3, 4, 10, 20, 5]  };
    println!("Min element: {} \nMax Elemet: {}", min_max_el.min(), min_max_el.max());
}
