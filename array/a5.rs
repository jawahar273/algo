// Topic: Move all the negative elements to one side of the array 

#[derive(PartialEq, PartialOrd)]
struct Array<T> { elements: Vec<T> }

impl<T: Ord> Array<T> {
    fn sort(&mut self) {
        self.elements.sort();
    }
}

fn main() {
    let mut array  = Array { elements: vec![-12, 9, 324, -3412, 4] };
    array.sort();
    println!("Move all the negative elements to one side of the array: {:?}", array.elements);
}
