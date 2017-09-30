package com.hust.grid.leesf.main;

public class QuickSort {
    public static void main(String[] args) {
        int[] array = {5, 2, 1, 3, 10, 14, 12, 43, 100, 105};
        quickSort(array, 0, array.length - 1);
        for (int i : array) {
            System.out.print(i + " ");
        }
    }

    public static void quickSort(int[] array, int left, int right) {
        if (left == right)
            return;
        int index = getPosition(array, left, right);
        if (index > left)
            quickSort(array, left, index - 1);
        if (index < right)
            quickSort(array, index + 1, right);

    }

    public static int getPosition(int[] array, int left, int right) {
        int key = array[left];
        while (left < right) {
            while (array[right] > key && (left < right))
                right--;
            array[left] = array[right];
            while (array[left] < key && (left < right))
                left++;
            array[right] = array[left];
        }
        array[left] = key;
        return left;
    }
}