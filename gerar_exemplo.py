#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para gerar arquivo Excel de exemplo com coordenadas e quantidades para heatmaps
Execute: python gerar_exemplo.py
"""

import pandas as pd
import random

def criar_exemplo_heatmap():
    """Cria arquivo Excel com coordenadas e quantidades para demonstrar heatmaps"""
    
    # Dados de exemplo - cidades brasileiras com população aproximada
    dados_exemplo = [
        # Região Sudeste (alta densidade)
        {'latitude': -23.5558, 'longitude': -46.6396, 'descricao': 'São Paulo - SP', 'quantidade': 12400000},
        {'latitude': -22.9068, 'longitude': -43.1729, 'descricao': 'Rio de Janeiro - RJ', 'quantidade': 6750000},
        {'latitude': -19.9167, 'longitude': -43.9345, 'descricao': 'Belo Horizonte - MG', 'quantidade': 2530000},
        {'latitude': -22.5504, 'longitude': -44.1019, 'descricao': 'Nova Iguaçu - RJ', 'quantidade': 820000},
        {'latitude': -23.2237, 'longitude': -45.9009, 'descricao': 'São José dos Campos - SP', 'quantidade': 695000},
        {'latitude': -22.8305, 'longitude': -47.0608, 'descricao': 'Campinas - SP', 'quantidade': 1200000},
        {'latitude': -23.9618, 'longitude': -46.3322, 'descricao': 'Santos - SP', 'quantidade': 433000},
        
        # Região Sul (média densidade)
        {'latitude': -25.4284, 'longitude': -49.2733, 'descricao': 'Curitiba - PR', 'quantidade': 1950000},
        {'latitude': -30.0346, 'longitude': -51.2177, 'descricao': 'Porto Alegre - RS', 'quantidade': 1490000},
        {'latitude': -27.5954, 'longitude': -48.5480, 'descricao': 'Florianópolis - SC', 'quantidade': 508000},
        {'latitude': -26.9194, 'longitude': -49.0661, 'descricao': 'Blumenau - SC', 'quantidade': 361000},
        {'latitude': -25.0955, 'longitude': -50.1658, 'descricao': 'Ponta Grossa - PR', 'quantidade': 355000},
        
        # Região Nordeste (média densidade)
        {'latitude': -12.9714, 'longitude': -38.5014, 'descricao': 'Salvador - BA', 'quantidade': 2900000},
        {'latitude': -8.0476, 'longitude': -34.8770, 'descricao': 'Recife - PE', 'quantidade': 1650000},
        {'latitude': -3.7319, 'longitude': -38.5267, 'descricao': 'Fortaleza - CE', 'quantidade': 2700000},
        {'latitude': -9.6658, 'longitude': -35.7353, 'descricao': 'Maceió - AL', 'quantidade': 1025000},
        {'latitude': -7.2399, 'longitude': -35.8811, 'descricao': 'João Pessoa - PB', 'quantidade': 820000},
        {'latitude': -5.7945, 'longitude': -35.2110, 'descricao': 'Natal - RN', 'quantidade': 890000},
        {'latitude': -2.5307, 'longitude': -44.3068, 'descricao': 'São Luís - MA', 'quantidade': 1100000},
        
        # Região Centro-Oeste (baixa densidade)
        {'latitude': -15.7934, 'longitude': -47.8828, 'descricao': 'Brasília - DF', 'quantidade': 3050000},
        {'latitude': -15.6014, 'longitude': -56.0979, 'descricao': 'Cuiabá - MT', 'quantidade': 1350000},
        {'latitude': -16.6799, 'longitude': -49.2550, 'descricao': 'Goiânia - GO', 'quantidade': 1540000},
        {'latitude': -20.4697, 'longitude': -54.6201, 'descricao': 'Campo Grande - MS', 'quantidade': 920000},
        
        # Região Norte (baixa densidade)
        {'latitude': -3.1190, 'longitude': -60.0217, 'descricao': 'Manaus - AM', 'quantidade': 2250000},
        {'latitude': -1.4558, 'longitude': -48.4902, 'descricao': 'Belém - PA', 'quantidade': 1500000},
        {'latitude': -5.0892, 'longitude': -42.8019, 'descricao': 'Teresina - PI', 'quantidade': 870000},
        {'latitude': -9.9754, 'longitude': -67.8243, 'descricao': 'Rio Branco - AC', 'quantidade': 420000},
        {'latitude': 2.8235, 'longitude': -60.6758, 'descricao': 'Boa Vista - RR', 'quantidade': 420000},
        {'latitude': -0.0389, 'longitude': -51.0664, 'descricao': 'Macapá - AP', 'quantidade': 520000},
        {'latitude': -10.1841, 'longitude': -48.3336, 'descricao': 'Palmas - TO', 'quantidade': 310000},
    ]
    
    # Criar DataFrame
    df = pd.DataFrame(dados_exemplo)
    
    # Salvar arquivo Excel
    nome_arquivo = 'exemplo_heatmap_brasil.xlsx'
    df.to_excel(nome_arquivo, index=False, engine='openpyxl')
    
    print(f"✅ Arquivo de exemplo para heatmap criado: {nome_arquivo}")
    print(f"📊 Total de pontos: {len(dados_exemplo)}")
    print(f"🔥 Ideal para mapas de calor e círculos proporcionais")
    print("\nColunas do arquivo:")
    print("- latitude: Coordenada de latitude")
    print("- longitude: Coordenada de longitude") 
    print("- descricao: Descrição do local")
    print("- quantidade: População (para heatmap/círculos)")
    
    # Mostrar preview dos dados
    print(f"\nPreview dos primeiros 5 pontos:")
    print(df.head().to_string(index=False))
    
    # Estatísticas
    print(f"\nEstatísticas da quantidade:")
    print(f"- Mínimo: {df['quantidade'].min():,}")
    print(f"- Máximo: {df['quantidade'].max():,}")
    print(f"- Média: {df['quantidade'].mean():,.0f}")
    print(f"- Total: {df['quantidade'].sum():,}")
    
    return nome_arquivo

def criar_exemplo_comercios():
    """Cria exemplo com dados comerciais fictícios"""
    
    # Simular dados de vendas de diferentes lojas
    cidades_comercio = [
        {'nome': 'Shopping Vila Velha', 'lat': -20.3297, 'lon': -40.2925, 'vendas': 2500000},
        {'nome': 'Shopping Iguatemi SP', 'lat': -23.5768, 'lon': -46.6891, 'vendas': 4200000},
        {'nome': 'Shopping Barra RJ', 'lat': -23.0045, 'lon': -43.3198, 'vendas': 3800000},
        {'nome': 'Shopping Crystal', 'lat': -25.4372, 'lon': -49.2645, 'vendas': 1900000},
        {'nome': 'Shopping Del Rey', 'lat': -19.9281, 'lon': -43.9386, 'vendas': 2200000},
        {'nome': 'Shopping Recife', 'lat': -8.1193, 'lon': -34.9058, 'vendas': 1800000},
        {'nome': 'Shopping Iguatemi Salvador', 'lat': -12.9785, 'lon': -38.4651, 'vendas': 2100000},
        {'nome': 'Shopping Iguatemi Fortaleza', 'lat': -3.7421, 'lon': -38.5119, 'vendas': 1700000},
        {'nome': 'Shopping Conjunto Nacional', 'lat': -15.7942, 'lon': -47.8922, 'vendas': 2300000},
        {'nome': 'Shopping Norte Sul Plaza', 'lat': -5.0729, 'lon': -42.7811, 'vendas': 950000},
    ]
    
    dados_comercio = []
    for comercio in cidades_comercio:
        # Adicionar loja principal
        dados_comercio.append({
            'latitude': comercio['lat'],
            'longitude': comercio['lon'],
            'descricao': comercio['nome'],
            'quantidade': comercio['vendas']
        })
        
        # Adicionar algumas lojas próximas com vendas menores
        for i in range(3):
            lat_offset = random.uniform(-0.01, 0.01)
            lon_offset = random.uniform(-0.01, 0.01)
            vendas_menores = random.randint(200000, 800000)
            
            dados_comercio.append({
                'latitude': comercio['lat'] + lat_offset,
                'longitude': comercio['lon'] + lon_offset,
                'descricao': f"Filial {i+1} - {comercio['nome'].split()[1] if len(comercio['nome'].split()) > 1 else comercio['nome']}",
                'quantidade': vendas_menores
            })
    
    df_comercio = pd.DataFrame(dados_comercio)
    nome_arquivo = 'exemplo_vendas_comerciais.xlsx'
    df_comercio.to_excel(nome_arquivo, index=False, engine='openpyxl')
    
    print(f"\n✅ Exemplo comercial criado: {nome_arquivo}")
    print(f"📊 Total de pontos: {len(dados_comercio)}")
    print(f"💰 Dados de vendas em reais")
    
    return nome_arquivo

def criar_exemplo_clima():
    """Cria exemplo com dados climáticos"""
    
    # Dados de temperatura média anual de diferentes cidades
    dados_clima = [
        {'latitude': -1.4558, 'longitude': -48.4902, 'descricao': 'Belém - PA', 'quantidade': 26.8},
        {'latitude': -3.1190, 'longitude': -60.0217, 'descricao': 'Manaus - AM', 'quantidade': 27.4},
        {'latitude': -3.7319, 'longitude': -38.5267, 'descricao': 'Fortaleza - CE', 'quantidade': 26.6},
        {'latitude': -12.9714, 'longitude': -38.5014, 'descricao': 'Salvador - BA', 'quantidade': 25.9},
        {'latitude': -15.7934, 'longitude': -47.8828, 'descricao': 'Brasília - DF', 'quantidade': 21.2},
        {'latitude': -19.9167, 'longitude': -43.9345, 'descricao': 'Belo Horizonte - MG', 'quantidade': 20.8},
        {'latitude': -22.9068, 'longitude': -43.1729, 'descricao': 'Rio de Janeiro - RJ', 'quantidade': 23.7},
        {'latitude': -23.5558, 'longitude': -46.6396, 'descricao': 'São Paulo - SP', 'quantidade': 19.2},
        {'latitude': -25.4284, 'longitude': -49.2733, 'descricao': 'Curitiba - PR', 'quantidade': 16.5},
        {'latitude': -30.0346, 'longitude': -51.2177, 'descricao': 'Porto Alegre - RS', 'quantidade': 19.4},
    ]
    
    df_clima = pd.DataFrame(dados_clima)
    nome_arquivo = 'exemplo_temperatura_brasil.xlsx'
    df_clima.to_excel(nome_arquivo, index=False, engine='openpyxl')
    
    print(f"\n✅ Exemplo climático criado: {nome_arquivo}")
    print(f"📊 Total de pontos: {len(dados_clima)}")
    print(f"🌡️ Dados de temperatura média anual (°C)")
    
    return nome_arquivo

if __name__ == "__main__":
    print("🗺️ GERADOR DE ARQUIVOS EXCEL PARA HEATMAPS")
    print("=" * 60)
    
    try:
        # Verificar se pandas e openpyxl estão instalados
        import pandas as pd
        import openpyxl
        
        print("1. Criando exemplo de heatmap populacional...")
        arquivo_populacional = criar_exemplo_heatmap()
        
        print("\n2. Criando exemplo comercial...")
        arquivo_comercial = criar_exemplo_comercios()
        
        print("\n3. Criando exemplo climático...")
        arquivo_climatico = criar_exemplo_clima()
        
        print(f"\n🎯 CONCLUÍDO!")
        print(f"Arquivos criados:")
        print(f"- {arquivo_populacional} (população)")
        print(f"- {arquivo_comercial} (vendas)")
        print(f"- {arquivo_climatico} (temperatura)")
        print(f"\n🔥 Todos os arquivos são ideais para testar:")
        print(f"   • Mapas de calor")
        print(f"   • Círculos proporcionais")
        print(f"   • Marcadores tradicionais")
        
    except ImportError as e:
        print(f"❌ ERRO: Dependência faltando - {e}")
        print("\nPara resolver, execute:")
        print("pip install pandas openpyxl")
    
    except Exception as e:
        print(f"❌ ERRO INESPERADO: {e}")
        print("Verifique se tem permissão para criar arquivos na pasta atual.")