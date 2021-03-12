package com.luis.arquivo;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class Arquivo {
    
    private static String destino = "INSIRA O DESTINO DO ARQUIVO AQUI";

    public static List<String> lerArquivo() {
        List<String> dados = new ArrayList<>();

        try {
            BufferedReader reader = new BufferedReader(new InputStreamReader(new FileInputStream(destino), "UTF-8"));
            
            String linha = reader.readLine();
            
            while (linha != null) {
                dados.add(linha);
                linha = reader.readLine();
            }
            
            reader.close();
        } catch (Exception e) {
        }
        
        return dados;
    }
}
