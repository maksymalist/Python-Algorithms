const array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

const binarySearch = (array, target) => {
  let low = 0;
  let high = array.length - 1;

  while (low <= high) {
    const mid = Math.floor((low + high) / 2);
    if (array[mid] == target) {
      console.log(`Found ${target} at index ${mid}`);
      return mid;
    } else if (array[mid] < target) {
      low = array[mid] + 1;
    } else {
      high = array[mid] - 1;
    }
  }
  console.log(`${target} not found`);
  return -1;
};

binarySearch(array, 10);
