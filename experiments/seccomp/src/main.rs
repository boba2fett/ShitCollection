use std::io::Write;

use libseccomp::*;

fn main() -> Result<(), Box<dyn std::error::Error>> {

    let mut filter = ScmpFilterContext::new_filter(ScmpAction::Allow)?;

    let syscall = ScmpSyscall::from_name("open")?;
    filter.add_rule(ScmpAction::Notify, syscall)?;
    let syscall = ScmpSyscall::from_name("openat")?;
    filter.add_rule(ScmpAction::Notify, syscall)?;

    filter.load()?;

    let fd = filter.get_notify_fd().unwrap();

    let handler = std::thread::spawn(||{
        let file = std::fs::File::create("_allowed.txt");
        if let Ok(mut file) = file {
            file.write_all(b"Hello, world!").unwrap();
        }

        let file = std::fs::File::create("_forbidden.txt");

        match file {
            Ok(mut file) => file.write_all(b"Hello, world!").unwrap(),
            Err(err) => println!("Os Error: {}", err.raw_os_error().unwrap()),
        }
    });

    for _ in 0..2 {
        let req = ScmpNotifReq::receive(fd).unwrap();
    
        dbg!(req);

        let path_ptr = req.data.args[1];

        let path = unsafe{
            let path_ptr: *const u8 = std::mem::transmute(path_ptr);
            read_c_string(path_ptr)
        };

        println!("openat path: {}", path);

        let resp = if path == "_allowed.txt" {
            ScmpNotifResp::new_continue(req.id, ScmpNotifRespFlags::empty())
        }
        else {
            ScmpNotifResp::new_error(req.id, -10, ScmpNotifRespFlags::empty())
        };

        resp.respond(fd).unwrap();
    }

    handler.join().unwrap();
    Ok(())
}

unsafe fn read_c_string(ptr: *const u8) -> String {
    let mut string = String::new();

    let mut curr_ptr = ptr;
    while *curr_ptr != b'\0' {
        let char = std::ptr::read(curr_ptr);
        string.push(char as char);
        curr_ptr = curr_ptr.add(1);
    }

    string
}