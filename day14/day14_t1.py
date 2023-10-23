import os
import glob
import concurrent.futures
import pandas as pd
import xml.etree.ElementTree as ET
import functools
import time

all_folder_name = ['aca', 'dem', 'fic', 'news']
common_path = os.path.join(os.getcwd(), 'day14')
"""for name in all_folder_name:
    os.mkdir(os.path.join(common_path, name))"""

all_result = {}

def timing_decorator(__main__):
    """装饰器，用来记录时间"""

    def wrapper(): #还是没太搞懂，如果被装饰的函数有参数，要怎么来装饰。回头有时间再看看
        """中间的函数"""  #但是装饰器的大体思路，或者说作用，就是在要执行的函数前后进行一些小操作
        start = time.time()
        __main__()
        end = time.time()
        elapsed_time = end - start
        print(elapsed_time) 
    
    return wrapper #返回wrapper，则调用被装饰函数的时候，实际上用的是wrapper

def process_xml_file(xml_file, folder_name):
    """处理单个.xml文件"""
    result = {}
    try:
        tree = ET.parse(xml_file)
        root = tree.getroot()
        words = [elem.get("hw") for elem in root.findall(".//w[@hw]")]
        #result['filename'] = xml_file
        #result['word_count'] = len(words)
        for word in words:
            if not word in result:
                result[word] = 1
            else:
                result[word] += 1
        
        df = pd.DataFrame({'item' : result.keys(), 'cnt' : result.values()})
        name = os.path.basename(xml_file)
        name = os.path.splitext(name)[0]
        name += '.csv'
        folder_path = os.path.join(common_path, folder_name)
        df.to_csv(os.path.join(folder_path, name), index=False)
    except Exception as e:
        result['filename'] = xml_file
        result['error'] = str(e)



def process_folder(folder_path):
    """对一个文件夹内的所有文件进行处理，视为对一个文件夹进行处理"""
    xml_files = glob.glob(os.path.join(folder_path, "*.xml"))
    folder_Name = os.path.basename(folder_path)
    num_of_threads = 15
    #time = 0
    process_xml_file_with_name = functools.partial(process_xml_file, folder_name = folder_Name)
    with concurrent.futures.ThreadPoolExecutor(max_workers = num_of_threads) as thread_executor:
        (thread_executor.map(process_xml_file_with_name, xml_files))
    
    #print(time)

def process_in_one(folder_path):
    """把处理以后的结果放到一个.csv文件"""
    xml_files = glob.glob(os.path.join(folder_path, "*.xml"))
    #folder_Name = os.path.basename(folder_path)
    num_of_threads = 15
    #time = 0
    #process_xml_file_with_name = functools.partial(process_xml_file_in_one, folder_name = folder_Name)
    with concurrent.futures.ThreadPoolExecutor(max_workers = num_of_threads) as thread_executor:
        (thread_executor.map(process_xml_file_in_one, xml_files))

def process_xml_file_in_one(xml_file):
    """把处理单个xml文件的结果放到一个.csv文件里"""
    try:
        tree = ET.parse(xml_file)
        root = tree.getroot()
        words = [elem.get("hw") for elem in root.findall(".//w[@hw]")]
        #result['filename'] = xml_file
        #result['word_count'] = len(words)
        for word in words:
            if not word in all_result:
                all_result[word] = 1
            else:
                all_result[word] += 1
        
        
    except Exception as e:
        all_result['filename'] = xml_file
        all_result['error'] = str(e)


@timing_decorator
def __main__():
    input_dir = "/home/bluemouse/下载/python作业/download/Texts"  # 存放xml文件的目录
    sub_folder = [os.path.join(input_dir, sub_dir) for sub_dir in os.listdir(input_dir) if os.path.isdir(os\
    .path.join(input_dir, sub_dir))]
    #sub_sub = [sub_folder[0]]
    num_processes = 4  # 进程数

    """with concurrent.futures.ProcessPoolExecutor(max_workers=num_processes) as process_executor:
        process_executor.map(process_folder, sub_folder)"""
    """with concurrent.futures.ProcessPoolExecutor(max_workers=num_processes) as process_executor:
        process_executor.map(process_in_one, sub_sub)"""
    for i in range(4):
        process_in_one(sub_folder[i])

    df = pd.DataFrame({'item' : all_result.keys(), 'cnt' : all_result.values()})
    name = 'all'
    name += '.csv'
    result_path = os.path.join(common_path, name)
    df.to_csv(result_path, index=False)

if __name__ == '__main__':
    __main__()
