
// Topic: Write a program to cyclically rotate an array by one.

#[derive(PartialEq, PartialOrd)]
struct Array<T> { elements: Vec<T> }


impl<T> Array<T> {
    fn rotate(&mut self)  {
        let last_element = self.elements.pop().unwrap();
        self.elements.insert(0, last_element);
    }
}

fn main() {
    let mut array = Array { elements: vec![9, 8, 7, 6, 4, 2, 1, 3] };
    array.rotate();
    println!("{:?}", array.elements);
}

