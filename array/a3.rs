struct KSmallElement { elements: Vec<i64> }

impl KSmallElement {
    fn sorted(&mut self, k: usize) -> i64 {
        return self.elements[k-1];
    }
}

fn main() {
    let mut __array = KSmallElement{ elements: vec![4, 5, 6, 8, 1] };
    println!("Kth Small Element: {}", __array.sorted(3));
}
