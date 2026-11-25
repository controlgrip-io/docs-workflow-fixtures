use std::io::{self, Read};
fn main() { let mut input = String::new(); io::stdin().read_to_string(&mut input).unwrap(); println!("{{\"stream\":\"users\",\"data\":{{\"id\":1,\"runtime\":\"rust\"}}}}"); }
