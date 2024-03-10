package test;

import figure.*;

public class Main {
    public static void main(String[] args) {

        Forme[] forme= new Forme[4];
        Triangle t =new Triangle("triangle",34.2,1.5);
        t.aire();

        Rectangle rec = new Rectangle("Rectangle",10,2.8);
        rec.aire();

        Cercle cer = new Cercle("Cercle",4);
        cer.aire();

        Carre c = new Carre("Carre",9);
        c.aire();

        forme[0]=t;
        forme[1]=rec;
        forme[2]=cer;
        forme[3]=c;


        for (int i = 0; i < 4; i++) {
            System.out.println(forme[i].getNom());
            System.out.println("Aire :" + forme[i].aire());
        }


    }
}