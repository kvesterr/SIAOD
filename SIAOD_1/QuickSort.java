package com.company;

import java.util.LinkedList;

public class QuickSort {

    /** Поля **/

    private LinkedList<Integer> array = new LinkedList<>(); // Основной массив


    /** Конструктор **/

    public QuickSort(LinkedList<Integer> arr){
        array = arr;
    }


    /** Методы **/

    // Метод выбора опорного элемента
    public static int chooseB(int L, int R){
        int B = (L+R)/2;
        return B;
    }

    // Метод прогона по массиву
    public LinkedList<Integer> startIteration(int L, int R){
        int B = chooseB(L,R);
        int l = L;
        int r = R;

        while (l < r){
            while (l < B) {
                if (array.get(l) <= array.get(B)) { l++; }
                else { break; }
            }
            while (r > B){
                if (array.get(r) >= array.get(B)){ r--; }
                else{ break; }
            }
            // Замена элементов
            int f = array.get(l);
            array.set(l,array.get(r));
            array.set(r,f);
        }
        return array;
    }


    // Метод полной сортировки массива
    public LinkedList<Integer> doQuickSort(LinkedList<Integer> arr) {
        int L = 0;
        int R = arr.size() - 1;
        QuickSort quickSort = new QuickSort(arr);
        arr = quickSort.startIteration(L, R);
        while ((R - L) >= 1) {
            for (int i = 0; i < arr.size(); i++) {
                for (int j = arr.size()-1; j > 0; j--) {
                    L = i;
                    R = j;
                    arr = quickSort.startIteration(L, R);
                }
            }
        }
        return arr;
    }

    public void toStringQuick(){
        System.out.println(array);
    }
}