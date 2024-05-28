# Autor: Arthur Musskopf da Luz - 2024/01
## Trabalho 2 - RSA - SHA - AES

Execução dos programas: 
python3 part1.py
python3 part2.py

Ambiente testado:
- Ubuntu 22.04;
- Python 3.10.9;
- Bibliotecas pycrypto e hashlib.

Deixei todos os valores usados fixos no código, com os comentários de como obter/alterar.

----------------------------------------------------------
---------------------------------------------------------

### Parte 1:

e_a =  E6A45B1F1BFBD3DCD7CBD688D78BB47F
d_a =  5F3BCD861338FEEE97026F9DC974CD70F078981AFD210DE96A430A1F3E9CF2D32593641EF1A9A6D025121FE6C802DFDE3007ED607BFAF1DF1D74D6554B52C6193B4DCC6CEC2F82EEF962BA72EDCF74FBF986DCA1242EB602FBA2C6860FE7125553CF59F425B8B6542740CDE8F242EF33526ABBEA5D6C5975E0DDB0B19F52C036593D3084D9A0EFFE9633C2DB8640C2AF914F41406C54D05A7614C51B6426CC1CB127C9BCB53344915D0107E836A0D1FD2221F7CDC317E30076EB918EB77E73FDFD485D535633F8E460A08AB6E65FCF472B47882D8E114F1B8FFD9C9683FA706BA25B1BFEB3F43C5C60A6A98AE12CEDE7DD8DE282C46E14AC3782ECEBFF1B1323

N_a =  64910929F05B40EB213E6294D0777EA107D78A8DE8849C35ED1C2D4796344ABC6DAB3ED4B5046202F9C3E8B6A0D567C94C89E8419672BAE03AC67F4AE67D77B4D4B7374760CE7C7348072A3390560806C188DC46F4105AFD9E794239A890713A03A0BB812FCFF7B9E2DFCD02D6F7F1683CED1DF6B980AE4237871A160B8235E495ADBFFF7564F946967E8BA063F29D6862CCAA04F1F34AFFC4506DD037FBC1C6541F7759E1E714E8D93C55FD78E9525FE6D2FF0425C2434B6CC0C27FA59FDEBA9672E2B6DFE3EA56C2CECBBB6B22FCA06704E2CEBD70A223936F36C143426A1553BC4CD445FF4F71761A3953A71527A4CC3283C7A7F859A3AD8CC81FF6A7561D

s =  00E621977578D75D3992C9A0B988A42F

x = 10E057D5B7D278E4E06DB83B39E11BDCD7240F1691AD82A48DE342B91D934ED59D8863C2000A9E19D1F03B5376106C33321B86D775254253ED5B59D9808FB204188D774ACC828F86D8EE313DC8B0D21059439D048DBDE1E5255A097394ADBE3D1DB74E3C782FB78C27BDDE2E70ADCD80B91C2E3C2105298659BD027758F11A8243DF3081965D9EE2C596BE2058D10ACE15EF7A1F5915D8BB29833F9D3A27D5486821F9FDBD146529064E2BBE4C578FA21FD62FFE7254181B757DF23439BD7EBBE709BB4B884D55C56C75BF7BE8790E2B963130C9C8097C8A2211DC67C2D717723519500B690468AA028A7919B19963781DC962A04439901B3E9042E953DB2111

sig_x = 4DF239EE8EFD39C6B3EA2ACCFCEB5419FC57A4803724234FF65854044163BE6A964AA8C706871EEEEF980DBD40205018BEE50336257751DF8898F902D35E9D4CFC4A7779C9923C96B706F163BB031F4EDD23D0C47B4A2E563981E42F15F7C2DF39362DE7BD428A057F9AC302EE77898F32FBCE73DB78A308CC3A198BDE2A2F5EBF6E58FB47AEAB923BB06D192084B58F01457F56B6F3F61FACFFDBCB5D5353A746C5E38BD10C679E2E32D70D9E4149781A43B2913E2F7F067639692E90E9EF36C8E8CED4A4CBA807C15841EAF1B2A3497EB6111C5DA280F72BE689C5A18E0D4742F38AF463B65D7B5169AE7A75DE70118EEC562E4265E4FFF40D8E00798CDD0D

---------------------------------------------------------
---------------------------------------------------------

### Parte 2:

Mensagem recebida do professor: F62E9DE75607A205D4046DD551C7446FA8D5CEA7FC64A879A8AE286D546B479164302E0E14E56CAE8246B87647BEE5D4ABDE7B7BB69CA0EEC354895C40499601E6A0223B948BAA2E62CE9F6DD78BE599

Assinatura recebida do professor: 07A3689DDB08C8423A0AE7E1221CDE6DB84FAFB4FADAEF1110797247E2100F046F27096BBDB027EB307B36013A089218A4B6336149CD23205F490ADEEF4EB82AEED4BDF0CE72B152BB63C92BE6DEAAF8AFEDCCBE8B30266592BC94961326F278534334B2B105D7ED0E27F750318C54F2EA258ECA917BAD0B5A5E24941BA3FF6CBEF80C89BB26BBFA4C7F191C199B7EE0A32F863E149B4E5C39D97DA3D3A7DC314A01F438885CD6130A583277D7167A6B27189FBC963176486F11D3B3C8CBD32F90ABEEDC03646571F6D2990A793EA507B0F9EEDD431ADB6CB578FC217F511C248EBBA4C34C658F62846477DC505868F386D36FB4E14C2920B9213F1C2CB16FDD

IV aleatorio usado: FB0A4212E1B8C4C59B255300C2C13006

Mensagem decifrada: 'arthur agora inverte esta mensagem e envia ela de volta cifrada'

Mensagem invertida cifrada: FB0A4212E1B8C4C59B255300C2C130066AD87EE682AFD7C8D46C0D5FEA688400185223EF45A1512E3CA3F42802A6F2652CF062A1AE782A2CBF43462D4D9041824068A04ACFE9A4DEA7BC216C59549417

Minha assinatura da mensagem: 3151A9051F0DB17C3AA694AC3F97B36047FF9C4C8C8A88F073874F548E760220BF1DC580BA1DA73CA75350DDE5784EE0A28A5856055AAF29FC935F1167D7764B33E4ED791DFBF4723FFF5074838D96A35726E5486A65ECE95F2E3DC389201B3BBD4CFA05D3CB6020AF72FD1755A24A02960D38A528FAFEBDCA2B3B8D9A7C5A9AE64E3F84A52834AD76818C3A302F1FA574AC03E02EE9BB1A182E532ADF145A146BF9B381B78CF5C1BD150FD164D85C87F20DD384A4753E11712130FCA0A30CD32600CE146AAB383048CF4444434A93BA93108153C6FF40C092866DACBDBD83B219E642D2EEFDD746924EB6E7A40DD0B931E9BCA1314C309AD4A36E8B0CA6F28C

------------------------------------------------

2° Mensagem recebida = FB0A4212E1B8C4C59B255300C2C1300688D9C4597E4F886E382D1E5BC03D258F543177E6EAEBCACBAEBC81074699EC12801F8DA1BEEFD0DB440E0B1736A26486

2° Assinatura recebida = E8115EB7C2B0EF15F54DD8DAEAD2012839B1914DCF086BA91C420EF66ECA70F6E5341442E926FFFDFE82C50DAEFD945E8753E3A2ECE0E5C2AD32EF0CD8A9553CD17FF4AEFA8C443E57012ACD20B932AD59F169B21A1C23489D2B4A510599B391289C3AA8C866B18B92F00DC2A6F64B516F624D155BD7D49C4F3E8AE44F4F2B33FF9AB383BAEC54A614B355396FF297FA420DC013FC3FC20029899EDA0EA20D3697814C5FC547318A0BAB6D0BF38E874F905D7741480064A1771DAE8A62FF11388A2FD3BF60B06D0FB53DF4CF3398C96F507AB1EDD63F1CD47AB1C0FD53EFC0D6699DCDBC3952F4114AFC6E9429FF26F27C78BAC345410F16884C4117661901C

2° Mensagem decifrada: 'Muito bom. Funcionou perfeitamente. []s'

c_inv = FB0A4212E1B8C4C59B255300C2C1300688D9C4597E4F886E382D1E5BC03D258F543177E6EAEBCACBAEBC81074699EC12801F8DA1BEEFD0DB440E0B1736A26486

sig_h_inv =  E8115EB7C2B0EF15F54DD8DAEAD2012839B1914DCF086BA91C420EF66ECA70F6E5341442E926FFFDFE82C50DAEFD945E8753E3A2ECE0E5C2AD32EF0CD8A9553CD17FF4AEFA8C443E57012ACD20B932AD59F169B21A1C23489D2B4A510599B391289C3AA8C866B18B92F00DC2A6F64B516F624D155BD7D49C4F3E8AE44F4F2B33FF9AB383BAEC54A614B355396FF297FA420DC013FC3FC20029899EDA0EA20D3697814C5FC547318A0BAB6D0BF38E874F905D7741480064A1771DAE8A62FF11388A2FD3BF60B06D0FB53DF4CF3398C96F507AB1EDD63F1CD47AB1C0FD53EFC0D6699DCDBC3952F4114AFC6E9429FF26F27C78BAC345410F16884C4117661901C