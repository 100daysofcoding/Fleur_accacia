package figure;

import static java.lang.Math.*;

public class Cercle extends Forme{
    private double rayon;

    public Cercle(String nom, double rayon) {
        super(nom);
        this.rayon = rayon;
    }

    public double getRayon() {
        return rayon;
    }

    public void setRayon(double rayon) {
        this.rayon = rayon;
    }

    @Override
    public double aire() {
        return rayon*rayon*PI;
    }

    @Override
    public String toString() {
        return "Cercle{" +
                "rayon=" + rayon +
                '}';
    }
}
