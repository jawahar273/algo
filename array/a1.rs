struct Array { elements: Vec<i64>  }


impl Array {
    fn reverse(&mut self) {
        let mut start = 0;
        let mut end = self.elements.len() - 1;

        while start < end {
            let temp = self.elements[end];
            self.elements[end] = self.elements[start];
            self.elements[start] = temp; 
            start += 1;
            end -= 1;
        }
    }

    fn display(&self) {
        println!("Elemets  {:?}", self.elements);
    }
}


fn main() {

    let mut _array: Array = Array{ elements: vec![2, 3, 4, 5, 6]  };
    _array.reverse();
    _array.display();
}
