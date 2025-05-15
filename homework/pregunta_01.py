# pylint: disable=import-outside-toplevel
# pylint: disable=line-too-long
# flake8: noqa
"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

import zipfile
import os
import pandas as pd 
import glob    
    
def process_files(folder):
    data = {"phrase": [],
            "target": []}
    for subfolder in os.listdir(folder):
        subfolder_path = os.path.join(folder, subfolder)
        if os.path.isdir(subfolder_path):
            category = subfolder
            for file_name in os.listdir(subfolder_path):
                if file_name.endswith(".txt"):
                    file_path = os.path.join(subfolder_path, file_name)
                    with open(file_path, "r") as file:
                        content = file.read()
                    data["phrase"].append(content)
                    data["target"].append(category)
    return data
    
    

def pregunta_01():
    
    
    """
    La información requerida para este laboratio esta almacenada en el
    archivo "files/input.zip" ubicado en la carpeta raíz.
    Descomprima este archivo.

    Como resultado se creara la carpeta "input" en la raiz del
    repositorio, la cual contiene la siguiente estructura de archivos:


    ```
    train/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    test/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    ```

    A partir de esta informacion escriba el código que permita generar
    dos archivos llamados "train_dataset.csv" y "test_dataset.csv". Estos
    archivos deben estar ubicados en la carpeta "output" ubicada en la raiz
    del repositorio.

    Estos archivos deben tener la siguiente estructura:

    * phrase: Texto de la frase. hay una frase por cada archivo de texto.
    * sentiment: Sentimiento de la frase. Puede ser "positive", "negative"
      o "neutral". Este corresponde al nombre del directorio donde se
      encuentra ubicado el archivo.

    Cada archivo tendria una estructura similar a la siguiente:

    ```
    |    | phrase                                                                                                                                                                 | target   |
    |---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
    |  0 | Cardona slowed her vehicle , turned around and returned to the intersection , where she called 911                                                                     | neutral  |
    |  1 | Market data and analytics are derived from primary and secondary research                                                                                              | neutral  |
    |  2 | Exel is headquartered in Mantyharju in Finland                                                                                                                         | neutral  |
    |  3 | Both operating profit and net sales for the three-month period increased , respectively from EUR16 .0 m and EUR139m , as compared to the corresponding quarter in 2006 | positive |
    |  4 | Tampere Science Parks is a Finnish company that owns , leases and builds office properties and it specialises in facilities for technology-oriented businesses         | neutral  |
    ```


    """
    
    
    zip_file_path = "./files/input.zip"
    extract_path = "./input"
    root_path = "./input/input"
    output_directory= "./files/output"
    
    if not os.path.exists(extract_path):
        os.makedirs(extract_path)
        
        with zipfile.ZipFile(zip_file_path, "r") as zip_data:
            zip_data.extractall(extract_path)
    
    #recorrer la carpeta test
    test_path = os.path.join(root_path, "test")
    test_data = process_files(test_path)
    df_test = pd.DataFrame(test_data)
    df_path_test = os.path.join(output_directory, "test_dataset.csv")
    
    #Recorrer la carpeta train
    train_path = os.path.join(root_path, "train")
    train_data = process_files(train_path)
    df_train = pd.DataFrame(train_data)
    df_path_train = os.path.join(output_directory, "train_dataset.csv")
    
    #guardar los datos en output
    if os.path.exists(output_directory):
        files = glob.glob(f"{output_directory}/*")
        for file in files:
            os.remove(file)
        os.rmdir(output_directory)
    
    os.mkdir(output_directory)
    df_train.to_csv(df_path_train, index=False)
    df_test.to_csv(df_path_test, index=False)
    
    
    
if __name__ == "__main__":
    pregunta_01()
    