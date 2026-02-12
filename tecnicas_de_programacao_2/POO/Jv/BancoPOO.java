abstract class Conta{
    protected String nome;
    protected Float saldo;
    protected Float limite;

    public Conta(String nome, Float saldo, Float limite) {
        this.nome = nome;
        this.saldo = saldo;
        this.limite = limite;
    }

    public Float get_saldo(){
        return saldo;
    }
    public Float get_limite(){
        return limite;
    }
    public void set_saldo(Float valor){
        if(valor <= limite){
            saldo += valor;
        }
    }

    public abstract String ver_tipo();
}

class ContaCorrente extends Conta{
    public ContaCorrente(String nome, Float saldo, Float limite) {
        super(nome, saldo, limite);
    }
    @Override
    public String ver_tipo(){
        return "Conta corrente";
    }
}

class ContaDigital extends Conta{
    public ContaDigital(String nome, Float saldo, Float limite) {
        super(nome, saldo, limite);
    }
    @Override
    public String ver_tipo(){
        return "Conta digital";
    }
}

public class BancoPOO{
    public static void main(String[] args) {
        Conta contaC = new ContaCorrente("Arthur", 3000.90f, 2000.20f);
        Conta contaD = new ContaDigital("Arthur", 3000.90f, 2000.20f);

        System.out.println(contaC.ver_tipo());
        System.out.println(contaC.get_limite());
        contaC.set_saldo(1999.99f);
        System.out.println(contaD.get_saldo());

        System.out.println(contaD.ver_tipo());
        System.out.println(contaD.get_limite());
        contaD.set_saldo(1999.99f);
        System.out.println(contaD.get_saldo());
}
}