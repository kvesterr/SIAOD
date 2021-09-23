package com.company;

import java.lang.reflect.Array;
import java.util.Arrays;
import java.util.Comparator;
import java.util.LinkedList;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        int method;
        Scanner in = new Scanner(System.in);
        LinkedList<Integer> linkedList = new LinkedList<Integer>();
        String str = in.next();
        while (!str.contentEquals("stop")) {
            linkedList.add(Integer.parseInt(str));
            str = in.next();
        }
        System.out.println("Выберите метод сортировки:\n1.Турнирная сортировка\n2.Быстрая соритровка\n3.Стандартная сортировка");
        str = in.next();
        method = Integer.parseInt(str);
        if (method == 1) {
            TournamentSort tournamentSort = new TournamentSort(linkedList);
            long startTime = System.nanoTime();
            tournamentSort.doSort();
            long time = System.nanoTime() - startTime;
            tournamentSort.toStringMain();
            System.out.println("На сортировку потрачено - " + time + " наносекунд");
        }
        else if (method == 2){
            QuickSort quickSort = new QuickSort(linkedList);
            long startTime = System.nanoTime();
            quickSort.doQuickSort(linkedList);
            long time = System.nanoTime() - startTime;
            quickSort.toStringQuick();
            System.out.println("На сортировку потрачено - " + time + " наносекунд");
        }
        else{
            int[] arr = new int[linkedList.size()];
            for (int i = 0;i < linkedList.size(); i++){
               arr[i] = linkedList.get(i);
            }
            long startTime = System.nanoTime();
            Arrays.sort(arr);
            long time = System.nanoTime() - startTime;
            System.out.print("[");
            for (int i = 0; i < arr.length; i++) {
                if ((i+1)!=arr.length)
                    System.out.print(arr[i]+", ");
                else
                    System.out.print(arr[i]);
            }
            System.out.println("]");
            System.out.println("На сортировку потрачено - " + time + " наносекунд");
        }
    }
}
