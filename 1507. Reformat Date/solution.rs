impl Solution {
    pub fn reformat_date(date: String) -> String {
        // Pre-split on spaces.
        let split : Vec<&str> = date.split_whitespace().collect();
        
        // Set the year.
        let year = split[2];
        
        // Set the month.
        let month = match split[1] {
            "Jan" => "01",
            "Feb" => "02",
            "Mar" => "03",
            "Apr" => "04",
            "May" => "05",
            "Jun" => "06",
            "Jul" => "07",
            "Aug" => "08",
            "Sep" => "09",
            "Oct" => "10",
            "Nov" => "11",
            "Dec" => "12",
            _=> unreachable!(),
        };
        
        // Set the day.
        let mut day = split[0].replace("th", "").replace("nd", "").replace("st", "").replace("rd","");
        if day.len() == 1 {
            day = "0".to_string() + &day;
        }
        
        // Use the format macro to output the correct format.
        format!("{}-{}-{:02}", year, month, day)
    }
}
