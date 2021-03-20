impl Solution {
    pub fn flip_and_invert_image(image: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let mut temp = 0;
        let size = image.len();
        let mut new_image = image;
        let mut temp2: Vec<i32>;
        for ii in (0..size) {
            for jj in (0..(size / 2)) {
                temp = new_image[ii][jj];
                new_image[ii][jj] = new_image[ii][size - jj - 1];
                new_image[ii][size - jj - 1] = temp;
            }
        }
        for kk in (0..(size / 2)) {
            temp2 = new_image[kk];
            new_image[kk] = new_image[size - 1 - kk];
            new_image[size - 1 - kk] = temp2;
        }
        return new_image;
    }
}
