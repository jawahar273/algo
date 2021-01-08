

struct Array { contents: Vec<i64>  }

impl Array {
    fn size(&self) -> usize {
        self.contents.len()
    }

    fn is_empty(&self) -> bool {
       self.contents.is_empty()
    } 

    fn at(&self, index: usize) -> i64 {
        self.contents[index]
    }
    
    fn display(&self) {
        println!("{:?}", self.contents);
    }

    fn push(&mut self, element: i64) {
        self.contents.push(element);
    } 

    fn insert(&mut self, index: usize, element: i64) {
        self.contents.insert(index, element);
    }

}

fn main() {
    let mut test_array: Array = Array{  contents: vec![1, 2, 4, 10] };
    println!("is_empty: {}, \n at: {}", test_array.is_empty(), test_array.at(1));
    test_array.display();
    test_array.push(100);
    test_array.insert(3, 200);
    test_array.display();
}



