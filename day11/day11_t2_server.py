import threading
import socket
from baidu_trans import baidu_api #对照着这个文件来看，很多细节需要修改
#其实引入它就是想用baidu_api里面的Translator类

translator = baidu_api.Translator()

def translate_text(src_lang, target_lang, text): #这个参数的顺序很重要，最好按照baidu_api里面的顺序来，不然就要改
    #那个文件里面的顺序了，会麻烦一点
    """把文本翻译成指定语言并返回"""
    return translator.translate(src_lang, target_lang, text)

def process(client_socket:socket):
    """处理客户端需求"""
    request = client_socket.recv(4096).decode() #从client_socket中获取数据，也就是从客户端获取需求；
    #注意这里需要解码，因为通信传的一般都是二进制数据，要解码成字符串，下面发送结果前要进行编码decode是一个道理
    src_lang, target_lang, text = request.split(',') #确定三个重要参数
    result = translator.translate(src_lang, target_lang, text)
    if result:
        client_socket.send(result['trans_result'][0]['dst'].encode()) #把结果发回客户端
    else:
        client_socket.send(b'')
    client_socket.close() #关闭当前套接字，释放资源

def main():
    """启动服务器"""
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('127.0.0.1', 12345)) #把服务器绑定到本地的12345端口，到时候客户端也往这里发消息
    server.listen(5) #表示服务器一次最多接收5个需求，再多就先不收了，处理完了再接收


    while True: #一般服务器都是一直运行的，所以会while True
        client, addr = server.accept() #client是一个套接字， addr是一个元组，包含客户端的地址和端口信息，第一个是地址，
        #第二个是端口
        print('listening on 127.0.0.1, 12345') #用来测试客户端是否成功连接上服务器
        handler = threading.Thread(target = process, args = (client, )) #参数要用元组形式
        handler.start()


if __name__ == '__main__':
    main()