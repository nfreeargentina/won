#! / usr / bin / env python
# - * - codificación: utf-8 - * -
# Copyright 2012-2018 Matt Martz
# Todos los derechos reservados.
# #
# Licenciado bajo la Licencia Apache, Versión 2.0 (la "Licencia"); puedes
# no usar este archivo excepto en cumplimiento con la Licencia. Puede obtener
# una copia de la Licencia en
# #
# http://www.apache.org/licenses/LICENSE-2.0
# #
# A menos que sea requerido por la ley aplicable o acordado por escrito, el software
# distribuido bajo la Licencia se distribuye "TAL CUAL", SIN
# GARANTÍAS O CONDICIONES DE CUALQUIER TIPO, ya sea expresa o implícita. Ver el
# Licencia para el idioma específico que rige los permisos y limitaciones
# bajo la licencia.

importar  os
importar  re
importar  csv
importación  sys
 matemáticas de importación
importar  errno
 señal de importación
 zócalo de importación
importación  timeit
 fecha y hora de importación
 plataforma de importación
 subprocesos de importación
importar  xml . analizadores . expatriado

prueba :
    importar  gzip
    GZIP_BASE  =  gzip . GzipFile
excepto  ImportError :
    gzip  =  Ninguno
    GZIP_BASE  =  objeto

__version__  =  '2.0.2'


clase  FakeShutdownEvent ( objeto ):
    "" "Clase para falsificar un subproceso. Evento.está configurado para que los usuarios de este módulo
    no están obligados a registrar sus propios subprocesos. Evento ()
    "" "

    @ método estático
    def  isSet ():
        "Método ficticio para devolver siempre falso" ""
        volver  falso


# Algunas variables globales que usamos
DEPURACIÓN  =  Falso
_GLOBAL_DEFAULT_TIMEOUT  =  object ()

# Comience el juego de importación para manejar Python 2 y Python 3
prueba :
    importar  json
excepto  ImportError :
    prueba :
        importar  simplejson  como  json
    excepto  ImportError :
        json  =  Ninguno

prueba :
    importar  xml . etree . cElementTree  como  ET
excepto  ImportError :
    prueba :
        importar  xml . etree . ElementTree  como  ET
    excepto  ImportError :
        de  xml . dom  import  minidom  como  DOM
        de  xml . analizadores . importación de expatriados  ExpatError 
        ET  =  Ninguno

prueba :
    desde  urllib2  import ( urlopen , Request , HTTPError , URLError ,
                         AbstractHTTPHandler , ProxyHandler ,
                         HTTPDefaultErrorHandler , HTTPRedirectHandler ,
                         HTTPErrorProcessor , OpenerDirector )
excepto  ImportError :
    de  urllib . solicitud de  importación ( urlopen , Request , HTTPError , URLError ,
                                AbstractHTTPHandler , ProxyHandler ,
                                HTTPDefaultErrorHandler , HTTPRedirectHandler ,
                                HTTPErrorProcessor , OpenerDirector )

prueba :
    desde  httplib  import  HTTPConnection , BadStatusLine
excepto  ImportError :
    de  http . importación de cliente  HTTPConnection , BadStatusLine 

prueba :
    desde  httplib  import  HTTPSConnection
excepto  ImportError :
    prueba :
        de  http . importación de cliente  HTTPSConnection 
    excepto  ImportError :
        HTTPSConnection  =  Ninguno

prueba :
    desde  cola  Cola de importación 
excepto  ImportError :
    de la  cola de  importación  Cola

prueba :
    desde  urlparse  import  urlparse
excepto  ImportError :
    de  urllib . analizar  importar  urlparse

prueba :
    desde  urlparse  import  parse_qs
excepto  ImportError :
    prueba :
        de  urllib . parse  import  parse_qs
    excepto  ImportError :
        de  cgi  import  parse_qs

prueba :
    de  hashlib  import  md5
excepto  ImportError :
    desde  md5  importar  md5

prueba :
    desde  argparse  importa  ArgumentParser  como  ArgParser
    de  argparse  importación  SUPRIMIR  como  ARG_SUPPRESS
    PARSER_TYPE_INT  =  int
    PARSER_TYPE_STR  =  str
    PARSER_TYPE_FLOAT  =  flotante
excepto  ImportError :
    desde  optparse  importar  OptionParser  como  ArgParser
    de  optparse  importación  SUPPRESS_HELP  como  ARG_SUPPRESS
    PARSER_TYPE_INT  =  'int'
    PARSER_TYPE_STR  =  'cadena'
    PARSER_TYPE_FLOAT  =  'flotante'

prueba :
    desde  cStringIO  import  StringIO
    BytesIO  =  Ninguno
excepto  ImportError :
    prueba :
        de  StringIO  importar  StringIO
        BytesIO  =  Ninguno
    excepto  ImportError :
        de  io  import  StringIO , BytesIO

prueba :
    importar  __builtin__
excepto  ImportError :
    Importar  construcciones
    desde  io  import  TextIOWrapper , FileIO

    clase  _Py3Utf8Output ( TextIOWrapper ):
        "" "UTF-8 envoltorio codificado alrededor de stdout para py3, para anular
        Stdout ASCII
        "" "
        def  __init__ ( self , f , ** kwargs ):
            buf  =  FileIO ( f . fileno (), 'w' )
            super ( _Py3Utf8Output , self ). __init__ (
                buf ,
                codificación = 'utf8' ,
                errores = 'estricto'
            )

        def  escribir ( self , s ):
            super ( _Py3Utf8Output , self ). escribir ( s )
            auto . rubor ()

    _py3_print  =  getattr ( incorporado , 'imprimir' )
    prueba :
        _py3_utf8_stdout  =  _Py3Utf8Output ( sys . stdout )
        _py3_utf8_stderr  =  _Py3Utf8Output ( sys . stderr )
    excepto  OSError :
        # sys.stdout / sys.stderr no es un objeto stdout / stderr compatible
        # solo utilízalo y espero que las cosas salgan bien
        _py3_utf8_stdout  =  sys . stdout
        _py3_utf8_stderr  =  sys . stderr

    def  to_utf8 ( v ):
        "" "No-op codifica a utf-8 para py3" ""
        volver  v

    def  print_ ( * args , ** kwargs ):
        "" "Función Wrapper para py3 para imprimir, con un stdout codificado utf-8" ""
        Si  kwargs . get ( 'archivo' ) ==  sys . stderr :
            kwargs [ 'file' ] =  _py3_utf8_stderr
        más :
            kwargs [ 'archivo' ] =  kwargs . get ( 'archivo' , _py3_utf8_stdout )
        _py3_print ( * args , ** kwargs )
más :
    del  __builtin__

    def  to_utf8 ( v ):
        "" "Codifique el valor a utf-8 si es posible para py2" ""
        prueba :
            volver  v . codificar ( 'utf8' , 'estricto' )
        excepto  AttributeError :
            volver  v

    def  print_ ( * args , ** kwargs ):
        "" "La función de impresión de nuevo estilo para Python 2.4 y 2.5.
        Tomado de https://pypi.python.org/pypi/six/
        Modificado para establecer la codificación en UTF-8 siempre y para vaciar después de escribir
        "" "
        fp  =  kwargs . pop ( "archivo" , sys . stdout )
        si  fp  es  Ninguno :
            regreso

        def  escribir ( datos ):
            si  no es  instancia ( datos , cadena base ):
                data  =  str ( datos )
            # Si el archivo tiene una codificación, codifique unicode con él.
            encoding  =  'utf8'   # Siempre confíe en UTF-8 para la salida
            if ( isinstance ( fp , archivo ) y
                    isinstance ( datos , unicode ) y
                    la codificación  no es  ninguna ): 
                errores  =  getattr ( fp , "errores" , ninguno )
                si los  errores  son  Ninguno :
                    errores  =  "estricto"
                datos  =  datos . codificar ( codificación , errores )
            fp . escribir ( datos )
            fp . rubor ()
        want_unicode  =  False
        sep  =  kwargs . pop ( "sep" , Ninguno )
        si  sep  no es  Ninguno : 
            if  isinstance ( sep , unicode ):
                want_unicode  =  True
            elif  no es  instancia ( sep , str ):
                raise  TypeError ( "sep debe ser None o una cadena" )
        fin  =  kwargs . pop ( "fin" , Ninguno )
        si el  final  no es  Ninguno : 
            if  isinstance ( final , unicode ):
                want_unicode  =  True
            elif  no es  instancia ( final , str ):
                raise  TypeError ( "el final debe ser None o una cadena" )
        si  kwargs :
            raise  TypeError ( "argumentos de palabra clave inválidos para imprimir ()" )
        si  no  want_unicode :
            para  arg  en  args :
                if  isinstance ( arg , unicode ):
                    want_unicode  =  True
                    descanso
        si  want_unicode :
            nueva línea  =  unicode ( " \ n " )
            espacio  =  unicode ( "" )
        más :
            nueva línea  =  " \ n "
            espacio  =  ""
        si  sep  es  None :
            sep  =  espacio
        si  final  es  Ninguno :
            fin  =  nueva línea
        para  i , arg  en  enumerate ( args ):
            si  yo :
                escribir ( sep )
            escribir ( arg )
        escribir ( fin )


# Excepción "constantes" para admitir Python 2 a Python 3
prueba :
    Importar  SSL
    prueba :
        CERT_ERROR  = ( ssl . CertificateError ,)
    excepto  AttributeError :
        CERT_ERROR  =  tupla ()

    HTTP_ERRORS  = (
        ( HTTPError , URLError , socket . Error , ssl . SSLError , BadStatusLine ) +
        CERT_ERROR
    )
excepto  ImportError :
    ssl  =  Ninguno
    HTTP_ERRORS  = ( HTTPError , URLError , socket . Error , BadStatusLine )


clase  SpeedtestException ( Excepción ):
    "" "Excepción base para este módulo" ""


clase  SpeedtestCLIError ( SpeedtestException ):
    "" "Excepción genérica para generar errores durante la operación CLI" ""


clase  SpeedtestHTTPError ( SpeedtestException ):
    "" "Excepción HTTP base para este módulo" ""


clase  SpeedtestConfigError ( SpeedtestException ):
    "" "El XML de configuración no es válido" ""


clase  SpeedtestServersError ( SpeedtestException ):
    "" "Los servidores XML no son válidos" ""


clase  ConfigRetrievalError ( SpeedtestHTTPError ):
    "" "No se pudo recuperar config.php" ""


Clase  ServersRetrievalError ( SpeedtestHTTPError ):
    "" "No se pudo recuperar speedtest-Server.php" ""


clase  InvalidServerIDType ( SpeedtestException ):
    "" "La ID del servidor utilizada para filtrar no era un entero" ""


clase  NoMatchedServers ( SpeedtestException ):
    "" "No hay servidores coincidentes al filtrar" ""


clase  SpeedtestMiniConnectFailure ( SpeedtestException ):
    "" "No se pudo conectar al miniservidor speedtest proporcionado" ""


clase  InvalidSpeedtestMiniServer ( SpeedtestException ):
    "" "El servidor proporcionado como un mini servidor de prueba rápida no aparece realmente
    ser un mini servidor más veloz
    "" "


clase  ShareResultsConnectFailure ( SpeedtestException ):
    "" "No se pudo conectar a la API speedtest.net para POSTAR resultados" ""


clase  ShareResultsSubmitFailure ( SpeedtestException ):
    "" "No se pueden POSTAR correctamente los resultados en la API speedtest.net después de
    conexión
    "" "


clase  SpeedtestUploadTimeout ( SpeedtestException ):
    "" "configuración de longitud de prueba alcanzada durante la carga
    Se utiliza para garantizar que la carga se detenga cuando no se deben enviar datos adicionales
    "" "


clase  SpeedtestBestServerFailure ( SpeedtestException ):
    "" "No se puede determinar el mejor servidor" ""


clase  SpeedtestMissingBestServer ( SpeedtestException ):
    "" "get_best_server no se llama o no se puede determinar el mejor servidor" ""


def  create_connection ( dirección , tiempo de espera = _GLOBAL_DEFAULT_TIMEOUT ,
                      source_address = None ):
    "" "Conéctese a * dirección * y devuelva el objeto de socket.
    Función de conveniencia. Conéctese a * dirección * (una tupla de 2 '' (host,
    puerto) ``) y devuelve el objeto de socket. Pasando lo opcional
    El parámetro * timeout * establecerá el tiempo de espera en la instancia del socket
    antes de intentar conectarse. Si no se proporciona * tiempo de espera *, el
    configuración de tiempo de espera predeterminada global devuelta por: func: `getdefaulttimeout`
    es usado Si * source_address * está configurado, debe ser una tupla de (host, puerto)
    para que el socket se una como dirección de origen antes de realizar la conexión.
    Un host de '' o puerto 0 le dice al sistema operativo que use el valor predeterminado.
    En gran parte enviado desde Python 2.7, modificado para trabajar con Python 2.4
    "" "

    host , puerto  =  dirección
    err  =  Ninguno
    para  res  en  zócalo . getaddrinfo ( host , puerto , 0 , socket . SOCK_STREAM ):
        af , tipo de calcetín , proto , nombre de canon , sa  =  res
        calcetín  =  ninguno
        prueba :
            calcetín  =  zócalo . zócalo ( af , tipo de calcetín , proto )
            si el  tiempo de espera  no es  _GLOBAL_DEFAULT_TIMEOUT : 
                calcetín . settimeout ( float ( timeout ))
            if  source_address :
                calcetín . enlace ( dirección_origen )
            calcetín . conectar ( sa )
             calcetín de regreso

        excepto  zócalo . error :
            err  =  get_exception ()
            si el  calcetín  no es  ninguno : 
                calcetín . cerrar ()

    si  err  no es  Ninguno : 
        elevar  err
    más :
        Levante el  zócalo . error ( "getaddrinfo devuelve una lista vacía" )


clase  SpeedtestHTTPConnection ( HTTPConnection ):
    "" "Conexión HTTP personalizada para admitir source_address en
    Python 2.4 - Python 3
    "" "
    def  __init__ ( self , * args , ** kwargs ):
        source_address  =  kwargs . pop ( 'source_address' , Ninguno )
        tiempo de espera  =  kwargs . pop ( 'tiempo de espera' , 10 )

        HTTPConnection . __init__ ( self , * args , ** kwargs )

        auto . source_address  =  source_address
        auto . tiempo de espera  =  tiempo de espera

    def  connect ( auto ):
        "" "Conéctese al host y al puerto especificados en __init__." ""
        prueba :
            auto . calcetín  =  zócalo . create_connection (
                ( self . host , self . port ),
                auto . tiempo de espera ,
                auto . Dirección de la fuente
            )
        excepto ( AttributeError , TypeError ):
            auto . calcetín  =  crear_conexión (
                ( self . host , self . port ),
                auto . tiempo de espera ,
                auto . Dirección de la fuente
            )


si  HTTPSConnection :
    clase  SpeedtestHTTPSConnection ( HTTPSConnection ,
                                   SpeedtestHTTPConnection ):
        "" "HTTPSConnection personalizada para admitir source_address en
        Python 2.4 - Python 3
        "" "
        def  __init__ ( self , * args , ** kwargs ):
            source_address  =  kwargs . pop ( 'source_address' , Ninguno )
            tiempo de espera  =  kwargs . pop ( 'tiempo de espera' , 10 )

            HTTPSConnection . __init__ ( self , * args , ** kwargs )

            auto . tiempo de espera  =  tiempo de espera
            auto . source_address  =  source_address

        def  connect ( auto ):
            "Conéctese a un host en un puerto (SSL) determinado".

            SpeedtestHTTPConnection . conectar ( auto )

            kwargs  = {}
            si  ssl :
                if  hasattr ( ssl , 'SSLContext' ):
                    kwargs [ 'server_hostname' ] =  self . anfitrión
                prueba :
                    auto . calcetín  =  auto . _contexto . wrap_socket ( self . sock , ** kwargs )
                excepto  AttributeError :
                    auto . calcetín  =  ssl . wrap_socket ( self . sock , ** kwargs )


def  _build_connection ( connection , source_address , timeout , context = None ):
    "" "Cross Python 2.4 - Python 3 invocable para construir una` `Conexión HTTP '' o
    `` HTTPSConnection`` con los argumentos que necesitamos
    Llamado de los métodos `` http (s) _open`` de `` SpeedtestHTTPHandler '' o
    `` SpeedtestHTTPSHandler``
    "" "
    def  inner ( host , ** kwargs ):
        kwargs . actualización ({
            'source_address' : source_address ,
            'timeout' : tiempo de espera
        })
        si  contexto :
            kwargs [ 'context' ] =  contexto
         conexión de retorno ( host , ** kwargs )
    volver  interior


clase  SpeedtestHTTPHandler ( AbstractHTTPHandler ):
    "" "Personalizado` `HTTPHandler`` que puede construir una` `Conexión HTTP '' con el
    Args que necesitamos para `` source_address`` y `` timeout``
    "" "
    def  __init__ ( self , debuglevel = 0 , source_address = None , timeout = 10 ):
        AbstractHTTPHandler . __init__ ( self , debuglevel )
        auto . source_address  =  source_address
        auto . tiempo de espera  =  tiempo de espera

    def  http_open ( self , req ):
        volver a  sí mismo . do_open (
            _build_connection (
                SpeedtestHTTPConnection ,
                auto . dirección_origen ,
                auto . se acabó el tiempo
            ),
            req
        )

    http_request  =  AbstractHTTPHandler . do_request_


clase  SpeedtestHTTPSHandler ( AbstractHTTPHandler ):
    "" "Custom` `HTTPSHandler`` que puede construir una` `HTTPSConnection`` con el
    Args que necesitamos para `` source_address`` y `` timeout``
    "" "
    def  __init__ ( self , debuglevel = 0 , context = None , source_address = None ,
                 tiempo de espera = 10 ):
        AbstractHTTPHandler . __init__ ( self , debuglevel )
        auto . _context  =  context
        auto . source_address  =  source_address
        auto . tiempo de espera  =  tiempo de espera

    def  https_open ( self , req ):
        volver a  sí mismo . do_open (
            _build_connection (
                SpeedtestHTTPSConnection ,
                auto . dirección_origen ,
                auto . tiempo de espera ,
                contexto = auto . _contexto ,
            ),
            req
        )

    https_request  =  AbstractHTTPHandler . do_request_


def  build_opener ( source_address = None , timeout = 10 ):
    "" "Función similar a` `urllib2.build_opener`` que generará
    un `` OpenerDirector`` con los controladores explícitos que queremos,
    `` source_address`` para encuadernación, `` timeout`` y nuestra costumbre
    `User-Agent`
    "" "

    impresora ( 'Tiempo de espera establecido en% d'  % de  tiempo de espera , depuración = Verdadero )

    if  source_address :
        source_address_tuple  = ( source_address , 0 )
        impresora ( 'Enlace a la dirección de origen:% r'  % ( source_address_tuple ,),
                depuración = verdadero )
    más :
        source_address_tuple  =  Ninguno

    manejadores  = [
        ProxyHandler (),
        SpeedtestHTTPHandler ( source_address = source_address_tuple ,
                             tiempo de espera = tiempo de espera ),
        SpeedtestHTTPSHandler ( source_address = source_address_tuple ,
                              tiempo de espera = tiempo de espera ),
        HTTPDefaultErrorHandler (),
        HTTPRedirectHandler (),
        HTTPErrorProcessor ()
    ]

    opener  =  OpenerDirector ()
    abridor . addheaders  = [( 'User-agent' , build_user_agent ())]

    para  manipulador  en  manipuladores :
        abridor . add_handler ( controlador )

     abridor de retorno


clase  GzipDecodedResponse ( GZIP_BASE ):
    "" "Un objeto tipo archivo para decodificar una respuesta codificada con el gzip
    método, como se describe en RFC 1952.
    Copiado en gran parte de `` xmlrpclib`` / `` xmlrpc.client`` y modificado
    para trabajar para py2.4-py3
    "" "
    def  __init__ ( auto , respuesta ):
        # la respuesta no admite tell () y read (), requerido por
        # GzipFile
        si  no es  gzip :
            raise  SpeedtestHTTPError ( 'el cuerpo de la respuesta HTTP está codificado con gzip'
                                     'pero el soporte de gzip no está disponible' )
        IO  =  BytesIO  o  StringIO
        auto . io  =  IO ()
        mientras que  1 :
            fragmento  =  respuesta . leer ( 1024 )
            si  len ( fragmento ) ==  0 :
                descanso
            auto . io . escribir ( trozo )
        auto . io . buscar ( 0 )
        gzip . GzipFile . __init__ ( self , mode = 'rb' , fileobj = self . io )

    def  cerrar ( auto ):
        prueba :
            gzip . GzipFile . cerca ( auto )
        por último :
            auto . io . cerrar ()


def  get_exception ():
    "" "Función auxiliar para trabajar con py2.4-py3 para obtener el actual
    excepción en un bloque try / except
    "" "
    volver  sys . exc_info () [ 1 ]


 distancia def ( origen , destino ):
    "" "Determine la distancia entre 2 conjuntos de [lat, lon] en km" ""

    lat1 , lon1  =  origen
    lat2 , lon2  =  destino
    radio  =  6371   # km

    dlat  =  matemática . radianes ( lat2  -  lat1 )
    dlon  =  matemática . radianes ( lon2  -  lon1 )
    a = (math.sin(dlat / 2) * math.sin(dlat / 2) +
         math.cos(math.radians(lat1)) *
         math.cos(math.radians(lat2)) * math.sin(dlon / 2) *
         math.sin(dlon / 2))
    c  =  2  *  matemáticas . atan2 ( math . sqrt ( a ), math . sqrt ( 1  -  a ))
    d  =  radio  *  c

    volver  d


def  build_user_agent ():
    "" "Crear una cadena de agente de usuario compatible con Mozilla / 5.0" ""

    ua_tuple  = (
        «Mozilla / 5.0» ,
        '(% s; U;% s; en-us)'  % ( plataforma . sistema (), plataforma . arquitectura () [ 0 ]),
         Plataforma 'Python /% s' %  . python_version (),
        '(KHTML, como Gecko)' ,
        'speedtest-cli /% s'  %  __version__
    )
    user_agent  =  '' . unirse ( ua_tuple )
    impresora ( 'User-Agent:% s'  %  user_agent , debug = True )
    return  user_agent


def  build_request ( url , data = None , headers = None , bump = '0' , secure = False ):
    "" "Crear un objeto de solicitud urllib2
    Esta función agrega automáticamente un encabezado User-Agent a todas las solicitudes
    "" "

    si  no  encabezados :
        encabezados  = {}

    if  url [ 0 ] ==  ':' :
        esquema  = ( 'http' , 'https' ) [ bool ( seguro )]
        schemed_url  =  '% s% s'  % ( esquema , url )
    más :
        schemed_url  =  url

    si  '?'  en  url :
        delim  =  '&'
    más :
        delim  =  '?'

    # ¿A QUIEN VAS A LLAMAR? ¡CACHE BUSTERS!
    final_url  =  '% s% sx =% s.% s'  % ( schemed_url , delim ,
                                 int ( timeit . time . time () *  1000 ),
                                 golpe )

    cabeceras . actualización ({
        'Cache-Control' : 'no-cache' ,
    })

    impresora ( '% s% s'  % (( 'GET' , 'POST' ) [ bool ( data )], final_url ),
            depuración = verdadero )

     Solicitud de devolución ( final_url , datos = datos , encabezados = encabezados )


def  catch_request ( solicitud , abridor = Ninguno ):
    "" "Función auxiliar para detectar excepciones comunes encontradas cuando
    establecer una conexión con una solicitud HTTP / HTTPS
    "" "

    si  abridor :
        _open  =  abridor . abierto
    más :
        _open  =  urlopen

    prueba :
        uh  =  _open ( solicitud )
        vuelve  eh , falso
    excepto  HTTP_ERRORS :
        e  =  get_exception ()
        no devuelva  ninguno , e


def  get_response_stream ( respuesta ):
    "" "Función auxiliar para devolver un lector Gzip si
    `` Content-Encoding`` es `` gzip`` de lo contrario, la respuesta en sí
    "" "

    prueba :
        getheader  =  respuesta . cabeceras . getheader
    excepto  AttributeError :
        getheader  =  respuesta . getheader

    if  getheader ( 'content-encoding' ) ==  'gzip' :
        return  GzipDecodedResponse ( respuesta )

    retorno de  la respuesta


def  get_attributes_by_tag_name ( dom , tag_name ):
    "" "Recuperar un atributo de un documento XML y devolverlo en un
    formato consistente
    Solo se usa con xml.dom.minidom, que probablemente solo se use
    con versiones de python anteriores a la 2.5
    "" "
    elem  =  dom . getElementsByTagName ( tag_name ) [ 0 ]
    return  dict ( list ( elem . atributos . items ()))


def  print_dots ( shutdown_event ):
    "" "Función de devolución de llamada incorporada utilizada por las clases de subprocesos para imprimir
    estado
    "" "
    def  inner ( current , total , start = False , end = False ):
        si  shutdown_event . isSet ():
            regreso

        sys . la salida estándar . escribir ( '.' )
        si  actual  +  1  ==  total  y  final  es  verdadero :
            sys . la salida estándar . escribir ( ' \ n ' )
        sys . la salida estándar . rubor ()
    volver  interior


def  do_nothing ( * args , ** kwargs ):
    pasar


clase  HTTPDownloader ( threading . Thread ):
    "" "Clase de subproceso para recuperar una URL" ""

    def  __init__ ( self , i , request , start , timeout , opener = None ,
                 shutdown_event = Ninguno ):
        enhebrado . Enhebrar . __init__ ( auto )
        auto . solicitud  =  solicitud
        auto . resultado  = [ 0 ]
        auto . hora de  inicio =  inicio
        auto . tiempo de espera  =  tiempo de espera
        auto . i  =  i
        si  abridor :
            auto . _opener  =  abridor . abierto
        más :
            auto . _opener  =  urlopen

        si  shutdown_event :
            auto . _shutdown_event  =  shutdown_event
        más :
            auto . _shutdown_event  =  FakeShutdownEvent ()

    def  run ( auto ):
        prueba :
            if ( timeit . default_timer () -  self . starttime ) <=  self . tiempo de espera :
                f  =  auto . _opener ( auto . petición )
                while ( no  self . _shutdown_event . isSet () y
                        ( timeit . default_timer () -  self . starttime ) <=
                        auto . tiempo de espera ):
                    auto . resultado . agregar ( len ( f . lectura ( 10240 )))
                    si  uno mismo . resultado [ - 1 ] ==  0 :
                        descanso
                f . cerrar ()
        excepto  IOError :
            pasar


clase  HTTPUploaderData ( objeto ):
    "" "Archivo como objeto para mejorar cortar la carga una vez que se agota el tiempo de espera
    ha sido conseguido
    "" "

    def  __init__ ( self , length , start , timeout , shutdown_event = None ):
        auto . longitud  =  longitud
        auto . inicio  =  inicio
        auto . tiempo de espera  =  tiempo de espera

        si  shutdown_event :
            auto . _shutdown_event  =  shutdown_event
        más :
            auto . _shutdown_event  =  FakeShutdownEvent ()

        auto . _data  =  Ninguno

        auto . total  = [ 0 ]

    def  pre_allocate ( self ):
        chars  =  '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        multiplicador  =  int ( round ( int ( self . length ) /  36.0 ))
        IO  =  BytesIO  o  StringIO
        prueba :
            auto . _data  =  IO (
                ( 'contenido1 =% s'  %
                 ( Caracteres  *  multiplicador ) [ 0 : int ( auto . De longitud ) -  9 ]
                 ) codificar ()
            )
        excepto  MemoryError :
            elevar  SpeedtestCLIError (
                'Memoria insuficiente para preasignar datos de carga. Por favor '
                'use --no-pre-allocate'
            )

    @ propiedad
     datos de def ( auto ):
        si  no  auto . _datos :
            auto . pre_allocate ()
        volver a  sí mismo . _datos

    def  read ( self , n = 10240 ):
        if (( timeit . default_timer () -  self . start ) <=  self . timeout  y
                no  auto . _shutdown_event . isSet ()):
            trozo  =  auto . los datos . leer ( n )
            auto . totales . agregar ( len ( fragmento ))
             trozo de retorno
        más :
            raise  SpeedtestUploadTimeout ()

    def  __len__ ( self ):
        volver a  sí mismo . longitud


clase  HTTPUploader ( threading . Thread ):
    "" "Clase de subproceso para poner una URL" ""

    def  __init__ ( self , i , request , start , size , timeout , opener = None ,
                 shutdown_event = Ninguno ):
        enhebrado . Enhebrar . __init__ ( auto )
        auto . solicitud  =  solicitud
        auto . solicitud . los datos . inicio  =  auto . hora de  inicio =  inicio
        auto . tamaño  =  tamaño
        auto . resultado  =  Ninguno
        auto . tiempo de espera  =  tiempo de espera
        auto . i  =  i

        si  abridor :
            auto . _opener  =  abridor . abierto
        más :
            auto . _opener  =  urlopen

        si  shutdown_event :
            auto . _shutdown_event  =  shutdown_event
        más :
            auto . _shutdown_event  =  FakeShutdownEvent ()

    def  run ( auto ):
        solicitud  =  auto . solicitud
        prueba :
            if (( timeit . default_timer () -  self . starttime ) <=  self . timeout  y
                    no  auto . _shutdown_event . isSet ()):
                prueba :
                    f  =  auto . _opener ( solicitud )
                excepto  TypeError :
                    # PY24 espera una cadena o búfer
                    # Esto también causa problemas con Ctrl-C, pero reconoceremos
                    # por el momento en que Ctrl-C en PY24 no es inmediato
                    request  =  build_request ( self . request . get_full_url (),
                                            datos = solicitud . los datos . lectura ( auto . de tamaño ))
                    f  =  auto . _opener ( solicitud )
                f . leer ( 11 )
                f . cerrar ()
                auto . resultado  =  suma ( auto . solicitud . datos . total )
            más :
                auto . resultado  =  0
        excepto ( IOError , SpeedtestUploadTimeout ):
            auto . resultado  =  suma ( auto . solicitud . datos . total )


clase  SpeedtestResults ( objeto ):
    "" "Clase para mantener los resultados de una prueba de velocidad, que incluye:
    Velocidad de Descarga
    Velocidad de carga
    Ping / Latencia para probar el servidor
    Datos sobre el servidor con el que se ejecutó la prueba
    Además, esta clase puede devolver datos de resultados como un diccionario o CSV,
    así como enviar una POST de los datos de resultados a la API de speedtest.net
    para obtener un enlace de imagen para compartir resultados.
    "" "

    def  __init__ ( self , download = 0 , upload = 0 , ping = 0 , server = None , client = None ,
                 abridor = Ninguno , seguro = Falso ):
        auto . descargar  =  descargar
        auto . cargar  =  cargar
        auto . ping  =  ping
        si el  servidor  es  Ninguno :
            auto . servidor  = {}
        más :
            auto . servidor  =  servidor
        auto . cliente  =  cliente  o {}

        auto . _share  =  Ninguno
        auto . timestamp  =  '% sZ'  %  datetime . fecha y hora utcnow (). isoformat ()
        auto . bytes_recibidos  =  0
        auto . bytes_sent  =  0

        si  abridor :
            auto . _opener  =  abridor
        más :
            auto . _opener  =  build_opener ()

        auto . _secure  =  seguro

    def  __repr__ ( self ):
        return  repr ( self . dict ())

    def  compartir ( auto ):
        "" "PUBLICAR datos en la API de speedtest.net para obtener resultados compartidos
        enlace
        "" "

        si  uno mismo . _ compartir :
            volver a  sí mismo . _compartir

        download  =  int ( round ( self . download  /  1000.0 , 0 ))
        ping  =  int ( round ( self . ping , 0 ))
        upload = int(round(self.upload / 1000.0, 0))

        # Build the request to send results back to speedtest.net
        # We use a list instead of a dict because the API expects parameters
        # in a certain order
        api_data = [
            'recommendedserverid=%s' % self.server['id'],
            'ping=%s' % ping,
            'screenresolution=',
            'promo=',
            'download=%s' % download,
            'screendpi=',
            'upload =% s'  %  upload ,
            'testmethod = http' ,
            'hash =% s'  %  md5 (( '% s-% s-% s-% s'  %
                             ( ping , carga , descarga , '297aae72' ))
                            . codificar ()). hexdigest (),
            'pantalla táctil = ninguna' ,
            'startmode = pingselect' ,
            'precisión = 1' ,
            'bytes recibidos =% s'  %  self . bytes_recibidos ,
            'bytessent =% s'  %  self . bytes_sentido ,
            'serverid =% s'  %  self . servidor [ 'id' ],
        ]

        encabezados  = { 'Referer' : 'http://c.speedtest.net/flash/speedtest.swf' }
        request  =  build_request ( ': //www.speedtest.net/api/api.php' ,
                                datos = '&' . unirse ( api_data ). codificar (),
                                encabezados = encabezados , seguro = auto . _secure )
        f , e  =  catch_request ( solicitud , abridor = self . _opener )
        si  e :
            elevar  ShareResultsConnectFailure ( e )

        respuesta  =  f . leer ()
        código  =  f . código
        f . cerrar ()

        si  int ( código ) ! =  200 :
            raise  ShareResultsSubmitFailure ( 'No se pudieron enviar resultados a'
                                            'speedtest.net' )

        qsargs  =  parse_qs ( respuesta . decodificación ())
        resultid  =  qsargs . get ( 'resultid' )
        si  no es  resultid  o  len ( resultid ) ! =  1 :
            raise  ShareResultsSubmitFailure ( 'No se pudieron enviar resultados a'
                                            'speedtest.net' )

        auto . _share  =  'http://www.speedtest.net/result/%s.png'  %  resultid [ 0 ]

        volver a  sí mismo . _compartir

    def  dict ( auto ):
        "" "Devolver diccionario de datos de resultados" ""

        volver {
            'descargar' : auto . descargar ,
            'subir' : auto . carga ,
            'ping' : auto . ping ,
            'servidor' : auto . servidor ,
            'marca de tiempo' : auto . marca de tiempo ,
            'bytes_sentido' : self . bytes_sentido ,
            'bytes_recibidos' : self . bytes_recibidos ,
            'compartir' : auto . _ compartir ,
            'cliente' : auto . cliente ,
        }

    @ método estático
    def  csv_header ( delimitador = ',' ):
        "" "Devolver encabezados CSV" ""

        fila  = [ 'ID del servidor' , 'Patrocinador' , 'Nombre del servidor' , 'Marca de tiempo' , 'Distancia' ,
               'Ping' , 'Descargar' , 'Cargar' , 'Compartir' , 'Dirección IP' ]
        out  =  StringIO ()
        escritor  =  csv . escritor ( fuera , delimitador = delimitador , lineterminator = '' )
        escritor . writerow ([ to_utf8 ( v ) para  v  en la  fila ])
        volver  a cabo . getvalue ()

    def  csv ( self , delimiter = ',' ):
        "" "Devolver datos en formato CSV" ""

        datos  =  auto . dict ()
        out  =  StringIO ()
        escritor  =  csv . escritor ( fuera , delimitador = delimitador , lineterminator = '' )
        fila  = [ datos [ 'servidor' ] [ 'id' ], datos [ 'servidor' ] [ 'patrocinador' ],
               datos [ 'servidor' ] [ 'nombre' ], datos [ 'marca de tiempo' ],
               datos [ 'servidor' ] [ 'd' ], datos [ 'ping' ], datos [ 'descargar' ],
               datos [ 'subir' ], auto . _share  o  '' , self . cliente [ 'ip' ]]
        escritor . writerow ([ to_utf8 ( v ) para  v  en la  fila ])
        volver  a cabo . getvalue ()

    def  json ( self , pretty = False ):
        "" "Devolver datos en formato JSON" ""

        kwargs  = {}
        si  bastante :
            kwargs . actualización ({
                'guión' : 4 ,
                'sort_keys' : verdadero
            })
        vuelve  json . vuelcos ( self . dict (), ** kwargs )


clase  Speedtest ( objeto ):
    "" "Clase para realizar operaciones de prueba estándar de speedtest.net" ""

    def  __init__ ( self , config = None , source_address = None , timeout = 10 ,
                 seguro = Falso , shutdown_event = Ninguno ):
        auto . config  = {}

        auto . _source_address  =  source_address
        auto . _timeout  =  timeout
        auto . _opener  =  build_opener ( source_address , timeout )

        auto . _secure  =  seguro

        si  shutdown_event :
            auto . _shutdown_event  =  shutdown_event
        más :
            auto . _shutdown_event  =  FakeShutdownEvent ()

        auto . get_config ()
        si  config  no es  None : 
            auto . config . actualizar ( config )

        auto . servidores  = {}
        auto . más cercano  = []
        auto . _best  = {}

        auto . resultados  =  SpeedtestResults (
            cliente = auto . config [ 'cliente' ],
            abridor = auto . _apertura ,
            seguro = seguro ,
        )

    @ propiedad
    def  mejor ( auto ):
        si  no  auto . _best :
            raise  SpeedtestMissingBestServer (
                'get_best_server no llamado o no puede determinar mejor'
                'servidor'
            )
        volver a  sí mismo . _mejor

    def  get_config ( self ):
        "" "Descargue la configuración de speedtest.net y devuelva solo los datos
        estamos interesados ​​en
        "" "

        encabezados  = {}
        si  gzip :
            encabezados [ 'Accept-Encoding' ] =  'gzip'
        request  =  build_request ( ': //www.speedtest.net/speedtest-config.php' ,
                                encabezados = encabezados , seguro = auto . _secure )
        uh , e  =  catch_request ( solicitud , abridor = self . _opener )
        si  e :
            elevar  ConfigRetrievalError ( e )
        configxml_list  = []

        stream  =  get_response_stream ( uh )

        mientras que  1 :
            prueba :
                configxml_list . agregar ( flujo . lectura ( 1024 ))
            excepto ( OSError , EOFError ):
                elevar  ConfigRetrievalError ( get_exception ())
            if  len ( configxml_list [ - 1 ]) ==  0 :
                descanso
        transmitir . cerrar ()
        eh . cerrar ()

        if  int ( uh . code ) ! =  200 :
            regresar  Ninguno

        configxml  =  '' . codificar (). unirse ( configxml_list )

        impresora ( 'Config XML: \ n % s'  %  configxml , debug = True )

        prueba :
            prueba :
                raíz  =  ET . fromstring ( configxml )
            excepto  ET . ParseError :
                e  =  get_exception ()
                raise  SpeedtestConfigError (
                    Configuración 'speedtest.net malformada:% s'  %  e
                )
            server_config  =  root . find ( 'server-config' ). attrib
            descargar  =  root . encontrar ( 'descargar' ). attrib
            upload  =  root . buscar ( 'subir' ). attrib
            # veces = root.find ('veces'). attrib
            cliente  =  root . encontrar ( 'cliente' ). attrib

        excepto  AttributeError :
            prueba :
                raíz  =  DOM . parseString ( configxml )
            excepto  ExpatError :
                e  =  get_exception ()
                raise  SpeedtestConfigError (
                    Configuración 'speedtest.net malformada:% s'  %  e
                )
            server_config  =  get_attributes_by_tag_name ( root , 'server-config' )
            download = get_attributes_by_tag_name(root, 'download')
            upload = get_attributes_by_tag_name(root, 'upload')
            # times = get_attributes_by_tag_name(root, 'times')
            client = get_attributes_by_tag_name(root, 'client')

        ignore_servers = list(
            map(int, server_config['ignoreids'].split(','))
        )

        ratio = int(upload['ratio'])
        upload_max = int(upload['maxchunkcount'])
        up_sizes = [32768, 65536, 131072, 262144, 524288, 1048576, 7340032]
        sizes = {
            'upload': up_sizes[ratio - 1:],
            'descarga' : [ 350 , 500 , 750 , 1000 , 1500 , 2000 , 2500 ,
                         3000 , 3500 , 4000 ]
        }

        size_count  =  len ( tamaños [ 'subir' ])

        upload_count  =  int ( matemáticas . ceil ( upload_max  /  SIZE_COUNT ))

        cuenta  = {
            'upload' : upload_count ,
            'descargar' : int ( descargar [ 'threadsperurl' ])
        }

        hilos  = {
            'upload' : int ( upload [ 'hilos' ]),
            'descargar' : int ( server_config [ 'threadcount' ]) *  2
        }

        longitud  = {
            'upload' : int ( upload [ 'testlength' ]),
            'descargar' : int ( descargar [ 'testlength' ])
        }

        auto . config . actualización ({
            'cliente' : cliente ,
            'ignore_servers' : ignore_servers ,
            'tamaños' : tamaños ,
            'cuenta' : cuenta ,
            'hilos' : hilos ,
            'length' : longitud ,
            'upload_max' : upload_count  *  size_count
        })

        prueba :
            auto . lat_lon  = ( float ( cliente [ 'lat' ]), float ( cliente [ 'lon' ]))
        excepto  ValueError :
            raise  SpeedtestConfigError (
                'Ubicación desconocida: lat =% r lon =% r'  %
                ( cliente . get ( 'lat' ), cliente . get ( 'lon' ))
            )

        impresora ( 'Config: \ n % r'  %  self . config , debug = True )

        volver a  sí mismo . config

    def  get_servers ( self , servidores = Ninguno , excluir = Ninguno ):
        "" "Recupere la lista de servidores speedtest.net, opcionalmente filtrados
        a servidores que coinciden con los especificados en el argumento `` servidores ''
        "" "
        si los  servidores  son  Ninguno :
            servidores  = []

        si  excluir  es  Ninguno :
            excluir  = []

        auto . servidores . claro ()

        para  server_list  en ( servidores , excluir ):
            para  i , s  en  enumerate ( server_list ):
                prueba :
                    lista_servidor [ i ] =  int ( s )
                excepto  ValueError :
                    raise  InvalidServerIDType (
                        '% s es un tipo de servidor no válido, debe ser int'  %  s
                    )

        urls  = [
            ': //www.speedtest.net/speedtest-servers-static.php' ,
            'http://c.speedtest.net/speedtest-servers-static.php' ,
            ': //www.speedtest.net/speedtest-servers.php' ,
            'http://c.speedtest.net/speedtest-servers.php' ,
        ]

        encabezados  = {}
        si  gzip :
            encabezados [ 'Accept-Encoding' ] =  'gzip'

        errores  = []
        para  url  en  urls :
            prueba :
                request  =  build_request (
                    '% s? hilos =% s'  % ( url ,
                                       auto . config [ 'hilos' ] [ 'descargar' ]),
                    encabezados = encabezados ,
                    seguro = auto . _seguro
                )
                uh , e  =  catch_request ( solicitud , abridor = self . _opener )
                si  e :
                    errores . agregar ( '% s'  %  e )
                    raise  ServersRetrievalError ()

                stream  =  get_response_stream ( uh )

                serverxml_list  = []
                mientras que  1 :
                    prueba :
                        serverxml_list . agregar ( flujo . lectura ( 1024 ))
                    excepto ( OSError , EOFError ):
                        raise  ServersRetrievalError ( get_exception ())
                    if  len ( Serverxml_list [ - 1 ]) ==  0 :
                        descanso

                transmitir . cerrar ()
                eh . cerrar ()

                if  int ( uh . code ) ! =  200 :
                    raise  ServersRetrievalError ()

                serverxml  =  '' . codificar (). unirse ( servidoresxml_list )

                impresora ( 'Servidores XML: \ n % s'  %  servidoresxml , depuración = Verdadero )

                prueba :
                    prueba :
                        prueba :
                            raíz  =  ET . fromstring ( servidoresxml )
                        excepto  ET . ParseError :
                            e  =  get_exception ()
                            raise  SpeedtestServersError (
                                Lista de servidores 'speedtest.net malformados:% s'  %  e
                            )
                        elementos  =  raíz . getiterator ( 'servidor' )
                    excepto  AttributeError :
                        prueba :
                            raíz  =  DOM . parseString ( Serverxml )
                        excepto  ExpatError :
                            e  =  get_exception ()
                            raise  SpeedtestServersError (
                                Lista de servidores 'speedtest.net malformados:% s'  %  e
                            )
                        elementos  =  raíz . getElementsByTagName ( 'servidor' )
                excepto ( SyntaxError , xml . parsers . expat . ExpatError ):
                    raise  ServersRetrievalError ()

                para  servidor  en  elementos :
                    prueba :
                        attrib  =  servidor . attrib
                    excepto  AttributeError :
                        attrib  =  dict ( lista ( servidor . atributos . elementos ()))

                    si los  servidores  e  int ( attrib . get ( 'id' )) no están  en los  servidores :
                        Seguir

                    if ( int ( attrib . get ( 'id' )) en  self . config [ 'ignore_servers' ]
                            o  int ( attrib . get ( 'id' )) en  exclude ):
                        Seguir

                    prueba :
                        d  =  distancia ( self . lat_lon ,
                                     ( float ( attrib . get ( 'lat' )),
                                      float ( attrib . get ( 'lon' ))))
                    excepto  Excepción :
                        Seguir

                    attrib [ 'd' ] =  d

                    prueba :
                        auto . servidores [ d ]. agregar ( attrib )
                    excepto  KeyError :
                        auto . servidores [ d ] = [ attrib ]

                descanso

            excepto  ServersRetrievalError :
                Seguir

        if ( servidores  o  excluir ) y  no  self . servidores :
            elevar  NoMatchedServers ()

        volver a  sí mismo . servidores

    def  set_mini_server ( self , server ):
        "" "En lugar de buscar una lista de servidores, establezca un enlace a un
        mini servidor speedtest
        "" "

        urlparts  =  urlparse ( servidor )

        nombre , ext  =  os . trayectoria . splitext ( urlparts [ 2 ])
        si  ext :
            url  =  os . trayectoria . dirname ( servidor )
        más :
            url  =  servidor

        request  =  build_request ( url )
        uh , e  =  catch_request ( solicitud , abridor = self . _opener )
        si  e :
            raise  SpeedtestMiniConnectFailure ( 'No se pudo conectar a% s'  %
                                              servidor )
        más :
            texto  =  uh . leer ()
            eh . cerrar ()

        extensión  =  re . findall ( 'upload _? [Ee] xtension: "([^"] +) "' ,
                               de texto . decodificar ())
        si  no  extensión :
            para  ext  en [ 'php' , 'asp' , 'aspx' , 'jsp' ]:
                prueba :
                    f  =  auto . _apertura . abierto (
                        '% s / speedtest / upload.% s'  % ( url , ext )
                    )
                excepto  Excepción :
                    pasar
                más :
                    datos  =  f . leer (). tira (). decodificar ()
                    if (f.code == 200 and
                            len(data.splitlines()) == 1 and
                            re.match('size=[0-9]', data)):
                        extension = [ext]
                        break
        if not urlparts or not extension:
            raise InvalidSpeedtestMiniServer('Invalid Speedtest Mini Server: '
                                             '%s' % server)

        self.servers = [{
            'sponsor': 'Speedtest Mini',
            'name': urlparts[1],
            'd': 0,
            'url': '%s/speedtest/upload.%s' % (url.rstrip('/'), extension[0]),
            'latency': 0,
            'id': 0
        }]

        return self.servers

    def get_closest_servers(self, limit=5):
        """Limit servers to the closest speedtest.net servers based on
        geographic distance
        """

        if not self.servers:
            self.get_servers()

        for d in sorted(self.servers.keys()):
            for s in self.servers[d]:
                self.closest.append(s)
                if len(self.closest) == limit:
                    break
            else:
                continue
            break

        printer('Closest Servers:\n%r' % self.closest, debug=True)
        return self.closest

    def get_best_server(self, servers=None):
        """Perform a speedtest.net "ping" to determine which speedtest.net
        server has the lowest latency
        """

        if not servers:
            if not self.closest:
                servers = self.get_closest_servers()
            servers = self.closest

        if self._source_address:
            source_address_tuple = (self._source_address, 0)
        else:
            source_address_tuple = None

        user_agent = build_user_agent()

        results = {}
        for server in servers:
            cum = []
            url = os.path.dirname(server['url'])
            stamp = int(timeit.time.time() * 1000)
            latency_url = '%s/latency.txt?x=%s' % (url, stamp)
            for i in range(0, 3):
                this_latency_url = '%s.%s' % (latency_url, i)
                printer('%s %s' % ('GET', this_latency_url),
                        debug=True)
                urlparts = urlparse(latency_url)
                try:
                    if urlparts[0] == 'https':
                        h = SpeedtestHTTPSConnection(
                            urlparts[1],
                            source_address=source_address_tuple
                        )
                    else:
                        h = SpeedtestHTTPConnection(
                            urlparts[1],
                            source_address=source_address_tuple
                        )
                    headers = {'User-Agent': user_agent}
                    path = '%s?%s' % (urlparts[2], urlparts[4])
                    start = timeit.default_timer()
                    h.request("GET", path, headers=headers)
                    r = h.getresponse()
                    total = (timeit.default_timer() - start)
                except HTTP_ERRORS:
                    e = get_exception()
                    printer('ERROR: %r' % e, debug=True)
                    cum.append(3600)
                    continue

                text = r.read(9)
                if int(r.status) == 200 and text == 'test=test'.encode():
                    cum.append(total)
                else:
                    cum.append(3600)
                h.close()

            avg = round((sum(cum) / 6) * 1000.0, 3)
            results[avg] = server

        try:
            fastest = sorted(results.keys())[0]
        except IndexError:
            raise SpeedtestBestServerFailure('Unable to connect to servers to '
                                             'test latency.')
        best = results[fastest]
        best['latency'] = fastest

        self.results.ping = fastest
        self.results.server = best

        self._best.update(best)
        printer('Best Server:\n%r' % best, debug=True)
        return best

    def download(self, callback=do_nothing):
        """Test download speed against speedtest.net"""

        urls = []
        for size in self.config['sizes']['download']:
            for _ in range(0, self.config['counts']['download']):
                urls.append('%s/random%sx%s.jpg' %
                            (os.path.dirname(self.best['url']), size, size))

        request_count = len(urls)
        requests = []
        for i, url in enumerate(urls):
            requests.append(
                build_request(url, bump=i, secure=self._secure)
            )

        def producer(q, requests, request_count):
            for i, request in enumerate(requests):
                thread = HTTPDownloader(
                    i,
                    request,
                    start,
                    self.config['length']['download'],
                    opener=self._opener,
                    shutdown_event=self._shutdown_event
                )
                thread.start()
                q.put(thread, True)
                callback(i, request_count, start=True)

        finished = []

        def consumer(q, request_count):
            while len(finished) < request_count:
                thread = q.get(True)
                while thread.isAlive():
                    thread.join(timeout=0.1)
                finished.append(sum(thread.result))
                callback(thread.i, request_count, end=True)

        q = Queue(self.config['threads']['download'])
        prod_thread = threading.Thread(target=producer,
                                       args=(q, requests, request_count))
        cons_thread = threading.Thread(target=consumer,
                                       args=(q, request_count))
        start = timeit.default_timer()
        prod_thread.start()
        cons_thread.start()
        while prod_thread.isAlive():
            prod_thread.join(timeout=0.1)
        while cons_thread.isAlive():
            cons_thread.join(timeout=0.1)

        stop = timeit.default_timer()
        self.results.bytes_received = sum(finished)
        self.results.download = (
            (self.results.bytes_received / (stop - start)) * 8.0
        )
        if self.results.download > 100000:
            self.config['threads']['upload'] = 8
        return self.results.download

    def upload(self, callback=do_nothing, pre_allocate=True):
        """Test upload speed against speedtest.net"""

        sizes = []

        for size in self.config['sizes']['upload']:
            for _ in range(0, self.config['counts']['upload']):
                sizes.append(size)

        # request_count = len(sizes)
        request_count = self.config['upload_max']

        requests = []
        for i, size in enumerate(sizes):
            # We set ``0`` for ``start`` and handle setting the actual
            # ``start`` in ``HTTPUploader`` to get better measurements
            data = HTTPUploaderData(
                size,
                0,
                self.config['length']['upload'],
                shutdown_event=self._shutdown_event
            )
            if pre_allocate:
                data.pre_allocate()
            requests.append(
                (
                    build_request(self.best['url'], data, secure=self._secure),
                    size
                )
            )

        def producer(q, requests, request_count):
            for i, request in enumerate(requests[:request_count]):
                thread = HTTPUploader(
                    i,
                    request[0],
                    start,
                    request[1],
                    self.config['length']['upload'],
                    opener=self._opener,
                    shutdown_event=self._shutdown_event
                )
                thread.start()
                q.put(thread, True)
                callback(i, request_count, start=True)

        finished = []

        def consumer(q, request_count):
            while len(finished) < request_count:
                thread = q.get(True)
                while thread.isAlive():
                    thread.join(timeout=0.1)
                finished.append(thread.result)
                callback(thread.i, request_count, end=True)

        q = Queue(self.config['threads']['upload'])
        prod_thread = threading.Thread(target=producer,
                                       args=(q, requests, request_count))
        cons_thread = threading.Thread(target=consumer,
                                       args=(q, request_count))
        start = timeit.default_timer()
        prod_thread.start()
        cons_thread.start()
        while prod_thread.isAlive():
            prod_thread.join(timeout=0.1)
        while cons_thread.isAlive():
            cons_thread.join(timeout=0.1)

        stop = timeit.default_timer()
        self.results.bytes_sent = sum(finished)
        self.results.upload = (
            (self.results.bytes_sent / (stop - start)) * 8.0
        )
        return self.results.upload


def ctrl_c(shutdown_event):
    """Catch Ctrl-C key sequence and set a SHUTDOWN_EVENT for our threaded
    operations
    """
    def inner(signum, frame):
        shutdown_event.set()
        printer('\nCancelling...', error=True)
        sys.exit(0)
    return inner


def version():
    """Print the version"""

    printer(__version__)
    sys.exit(0)


def csv_header(delimiter=','):
    """Print the CSV Headers"""

    printer(SpeedtestResults.csv_header(delimiter=delimiter))
    sys.exit(0)


def parse_args():
    """Function to handle building and parsing of command line arguments"""
    description = (
        'Command line interface for testing internet bandwidth using '
        'speedtest.net.\n'
        '------------------------------------------------------------'
        '--------------\n'
        'https://github.com/sivel/speedtest-cli')

    parser = ArgParser(description=description)
    # Give optparse.OptionParser an `add_argument` method for
    # compatibility with argparse.ArgumentParser
    try:
        parser.add_argument = parser.add_option
    except AttributeError:
        pass
    parser.add_argument('--no-download', dest='download', default=True,
                        action='store_const', const=False,
                        help='Do not perform download test')
    parser.add_argument('--no-upload', dest='upload', default=True,
                        action='store_const', const=False,
                        help='Do not perform upload test')
    parser.add_argument('--bytes', dest='units', action='store_const',
                        const=('byte', 8), default=('bit', 1),
                        help='Display values in bytes instead of bits. Does '
                             'not affect the image generated by --share, nor '
                             'output from --json or --csv')
    parser.add_argument('--share', action='store_true',
                        help='Generate and provide a URL to the speedtest.net '
                             'share results image, not displayed with --csv')
    parser.add_argument('--simple', action='store_true', default=False,
                        help='Suppress verbose output, only show basic '
                             'information')
    parser.add_argument('--csv', action='store_true', default=False,
                        help='Suppress verbose output, only show basic '
                             'information in CSV format. Speeds listed in '
                             'bit/s and not affected by --bytes')
    parser.add_argument('--csv-delimiter', default=',', type=PARSER_TYPE_STR,
                        help='Single character delimiter to use in CSV '
                             'output. Default ","')
    parser.add_argument('--csv-header', action='store_true', default=False,
                        help='Print CSV headers')
    parser.add_argument('--json', action='store_true', default=False,
                        help='Suppress verbose output, only show basic '
                             'information in JSON format. Speeds listed in '
                             'bit/s and not affected by --bytes')
    parser.add_argument('--list', action='store_true',
                        help='Display a list of speedtest.net servers '
                             'sorted by distance')
    parser.add_argument('--server', type=PARSER_TYPE_INT, action='append',
                        help='Specify a server ID to test against. Can be '
                             'supplied multiple times')
    parser.add_argument('--exclude', type=PARSER_TYPE_INT, action='append',
                        help='Exclude a server from selection. Can be '
                             'supplied multiple times')
    parser.add_argument('--mini', help='URL of the Speedtest Mini server')
    parser.add_argument('--source', help='Source IP address to bind to')
    parser.add_argument('--timeout', default=10, type=PARSER_TYPE_FLOAT,
                        help='HTTP timeout in seconds. Default 10')
    parser.add_argument('--secure', action='store_true',
                        help='Use HTTPS instead of HTTP when communicating '
                             'with speedtest.net operated servers')
    parser.add_argument('--no-pre-allocate', dest='pre_allocate',
                        action='store_const', default=True, const=False,
                        help='Do not pre allocate upload data. Pre allocation '
                             'is enabled by default to improve upload '
                             'performance. To support systems with '
                             'insufficient memory, use this option to avoid a '
                             'MemoryError')
    parser.add_argument('--version', action='store_true',
                        help='Show the version number and exit')
    parser.add_argument('--debug', action='store_true',
                        help=ARG_SUPPRESS, default=ARG_SUPPRESS)

    options = parser.parse_args()
    if isinstance(options, tuple):
        args = options[0]
    else:
        args = options
    return args


def validate_optional_args(args):
    """Check if an argument was provided that depends on a module that may
    not be part of the Python standard library.
    If such an argument is supplied, and the module does not exist, exit
    with an error stating which module is missing.
    """
    optional_args = {
        'json': ('json/simplejson python module', json),
        'secure': ('SSL support', HTTPSConnection),
    }

    for arg, info in optional_args.items():
        if getattr(args, arg, False) and info[1] is None:
            raise SystemExit('%s is not installed. --%s is '
                             'unavailable' % (info[0], arg))


def printer(string, quiet=False, debug=False, error=False, **kwargs):
    """Helper function print a string with various features"""

    if debug and not DEBUG:
        return

    if debug:
        if sys.stdout.isatty():
            out = '\033[1;30mDEBUG: %s\033[0m' % string
        else:
            out = 'DEBUG: %s' % string
    else:
        out = string

    if error:
        kwargs['file'] = sys.stderr

    if not quiet:
        print_(out, **kwargs)


def shell():
    """Run the full speedtest.net test"""

    global DEBUG
    shutdown_event = threading.Event()

    signal.signal(signal.SIGINT, ctrl_c(shutdown_event))

    args = parse_args()

    # Print the version and exit
    if args.version:
        version()

    if not args.download and not args.upload:
        raise SpeedtestCLIError('Cannot supply both --no-download and '
                                '--no-upload')

    if len(args.csv_delimiter) != 1:
        raise SpeedtestCLIError('--csv-delimiter must be a single character')

    if args.csv_header:
        csv_header(args.csv_delimiter)

    validate_optional_args(args)

    debug = getattr(args, 'debug', False)
    if debug == 'SUPPRESSHELP':
        debug = False
    if debug:
        DEBUG = True

    if args.simple or args.csv or args.json:
        quiet = True
    else:
        quiet = False

    if args.csv or args.json:
        machine_format = True
    else:
        machine_format = False

    # Don't set a callback if we are running quietly
    if quiet or debug:
        callback = do_nothing
    else:
        callback = print_dots(shutdown_event)

    printer('Retrieving speedtest.net configuration...', quiet)
    try:
        speedtest = Speedtest(
            source_address=args.source,
            timeout=args.timeout,
            secure=args.secure
        )
    except (ConfigRetrievalError,) + HTTP_ERRORS:
        printer('Cannot retrieve speedtest configuration', error=True)
        raise SpeedtestCLIError(get_exception())

    if args.list:
        try:
            speedtest.get_servers()
        except (ServersRetrievalError,) + HTTP_ERRORS:
            printer('Cannot retrieve speedtest server list', error=True)
            raise SpeedtestCLIError(get_exception())

        for _, servers in sorted(speedtest.servers.items()):
            for server in servers:
                line = ('%(id)5s) %(sponsor)s (%(name)s, %(country)s) '
                        '[%(d)0.2f km]' % server)
                try:
                    printer(line)
                except IOError:
                    e = get_exception()
                    if e.errno != errno.EPIPE:
                        raise
        sys.exit(0)

    printer('Testing from %(isp)s (%(ip)s)...' % speedtest.config['client'],
            quiet)

    if not args.mini:
        printer('Retrieving speedtest.net server list...', quiet)
        try:
            speedtest.get_servers(servers=args.server, exclude=args.exclude)
        except NoMatchedServers:
            raise SpeedtestCLIError(
                'No matched servers: %s' %
                ', '.join('%s' % s for s in args.server)
            )
        except (ServersRetrievalError,) + HTTP_ERRORS:
            printer('Cannot retrieve speedtest server list', error=True)
            raise SpeedtestCLIError(get_exception())
        except InvalidServerIDType:
            raise SpeedtestCLIError(
                '%s is an invalid server type, must '
                'be an int' % ', '.join('%s' % s for s in args.server)
            )

        if args.server and len(args.server) == 1:
            printer('Retrieving information for the selected server...', quiet)
        else:
            printer('Selecting best server based on ping...', quiet)
        speedtest.get_best_server()
    elif args.mini:
        speedtest.get_best_server(speedtest.set_mini_server(args.mini))

    results = speedtest.results

    printer('Hosted by %(sponsor)s (%(name)s) [%(d)0.2f km]: '
            '%(latency)s ms' % results.server, quiet)

    if args.download:
        printer('Testing download speed', quiet,
                end=('', '\n')[bool(debug)])
        speedtest.download(callback=callback)
        printer('Download: %0.2f M%s/s' %
                ((results.download / 1000.0 / 1000.0) / args.units[1],
                 args.units[0]),
                quiet)
    else:
        printer('Skipping download test', quiet)

    if args.upload:
        printer('Testing upload speed', quiet,
                end=('', '\n')[bool(debug)])
        speedtest.upload(callback=callback, pre_allocate=args.pre_allocate)
        printer('Upload: %0.2f M%s/s' %
                ((results.upload / 1000.0 / 1000.0) / args.units[1],
                 args.units[0]),
                quiet)
    else:
        printer('Skipping upload test', quiet)

    printer('Results:\n%r' % results.dict(), debug=True)

    if not args.simple and args.share:
        results.share()

    if args.simple:
        printer('Ping: %s ms\nDownload: %0.2f M%s/s\nUpload: %0.2f M%s/s' %
                (results.ping,
                 (results.download / 1000.0 / 1000.0) / args.units[1],
                 args.units[0],
                 (results.upload / 1000.0 / 1000.0) / args.units[1],
                 args.units[0]))
    elif args.csv:
        printer(results.csv(delimiter=args.csv_delimiter))
    elif args.json:
        printer(results.json())

    if args.share and not machine_format:
        printer('Share results: %s' % results.share())


def main():
    try:
        shell()
    except KeyboardInterrupt:
        printer('\nCancelling...', error=True)
    except (SpeedtestException, SystemExit):
        e = get_exception()
        # Ignore a successful exit, or argparse exit
        if getattr(e, 'code', 1) not in (0, 2):
            raise SystemExit('ERROR: %s' % e)


if __name__ == '__main__':
    main()
