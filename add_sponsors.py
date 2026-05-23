#!/usr/bin/env python3
"""
Script para agregar sponsors a DynamoDB
Uso: python add_sponsors.py
"""

import boto3
import uuid
import json
from botocore.exceptions import ClientError

# Configuración
TABLE_NAME = "networking-passport-argentina-db-table"  # Ajusta según tu stack name
REGION = "us-east-1"

# Lista de sponsors a agregar
SPONSORS = [
    {
        "sponsor_id": "2",
        "sponsor_name": "AWS",
        "key": str(uuid.uuid4()),
        "required": True
    },
    {
        "sponsor_id": "3",
        "sponsor_name": "Clouxter",
        "key": str(uuid.uuid4()),
        "required": True
    },
    {
        "sponsor_id": "4",
        "sponsor_name": "Crubyt",
        "key": str(uuid.uuid4()),
        "required": True
    },
        {
        "sponsor_id": "5",
        "sponsor_name": "Epam",
        "key": str(uuid.uuid4()),
        "required": True
    },
    {
        "sponsor_id": "6",
        "sponsor_name": "Ingram",
        "key": str(uuid.uuid4()),
        "required": True
    },
    {
        "sponsor_id": "7",
        "sponsor_name": "AWS Community Day",
        "key": str(uuid.uuid4()),
        "required": True
    },
        {
        "sponsor_id": "8",
        "sponsor_name": "Nequi",
        "key": str(uuid.uuid4()),
        "required": True
    },
    {
        "sponsor_id": "9",
        "sponsor_name": "Nix",
        "key": str(uuid.uuid4()),
        "required": True
    },
    {
        "sponsor_id": "10",
        "sponsor_name": "Unal",
        "key": str(uuid.uuid4()),
        "required": True
    }
]

def add_sponsor(dynamodb, sponsor_data):
    """Agrega un sponsor a DynamoDB"""
    try:
        item = {
            "PK": {"S": f"SPONSOR#{sponsor_data['sponsor_id']}"},
            "SK": {"S": "PROFILE"},
            "key": {"S": sponsor_data["key"]},
            "required": {"BOOL": sponsor_data["required"]},
            "sponsor_id": {"S": sponsor_data["sponsor_id"]},
            "sponsor_name": {"S": sponsor_data["sponsor_name"]}
        }
        
        response = dynamodb.put_item(
            TableName=TABLE_NAME,
            Item=item
        )
        
        print(f"✅ Sponsor agregado: {sponsor_data['sponsor_name']} (ID: {sponsor_data['sponsor_id']})")
        print(f"   Key: {sponsor_data['key']}")
        return True
        
    except ClientError as e:
        print(f"❌ Error agregando sponsor {sponsor_data['sponsor_name']}: {e}")
        return False

def main():
    """Función principal"""
    print("🚀 Agregando sponsors a DynamoDB...")
    print(f"📋 Tabla: {TABLE_NAME}")
    print(f"🌍 Región: {REGION}")
    print()
    
    # Inicializar cliente de DynamoDB
    dynamodb = boto3.client('dynamodb', region_name=REGION)
    
    # Verificar que la tabla existe
    try:
        dynamodb.describe_table(TableName=TABLE_NAME)
    except ClientError as e:
        print(f"❌ Error: La tabla {TABLE_NAME} no existe o no tienes permisos")
        print("💡 Asegúrate de que el backend esté desplegado y el nombre de la tabla sea correcto")
        return
    
    # Agregar sponsors
    success_count = 0
    for sponsor in SPONSORS:
        if add_sponsor(dynamodb, sponsor):
            success_count += 1
        print()
    
    print(f"🎉 Proceso completado: {success_count}/{len(SPONSORS)} sponsors agregados exitosamente")
    
    if success_count > 0:
        print("\n📝 Información de los sponsors agregados:")
        print("Guarda estas claves de forma segura:")
        for sponsor in SPONSORS:
            print(f"   {sponsor['sponsor_name']}: {sponsor['key']}")

if __name__ == "__main__":
    main() 