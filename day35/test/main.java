/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package Test;

import Restaurant.*;
import restaurant.FastFood;
import restaurant.Restaurant;

/**
 *
 * @author user
 */
public class Grassounet {

    public static void main(String[] args) {
        FastFood FF= new FastFood(15,"Lips",2,"Burger");
        Restaurant R= new Restaurant("EnBouche",3,"Nemmes");
        
        R.servir();
        System.out.println(R.toString());
        System.out.println("---------------------------------");
        FF.preparer();
        System.out.println(FF.toString());
        
        
      
    }
    
}
