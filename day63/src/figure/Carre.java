package figure;

public class Carre extends Forme{
    private double cote;

    public Carre(String nom,double cote) {
        super(nom);
        this.cote = cote;
    }

    public double getCote() {
        return cote;
    }

    public void setCote(double cote) {
        this.cote = cote;
    }

    @Override
    public double aire() {
        return cote*cote;
    }
}
