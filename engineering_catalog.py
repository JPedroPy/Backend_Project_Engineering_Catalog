import smtplib as smtp
import email.message as email

#Definition of a method for header formatting
def tracos(wrd):
    print('-' * 50)
    print(wrd.center(50))
    print('-' * 50)


#Creating lists and variables
Pedido = 'S'
Cliente = []
Valor = []
Produtos = []
Cont = 1

#Clients input data
nome = str(input('Enter your name: '))
gmail = str(input('Enter your email: '))
telefone = str(input('Enter your phone number: '))

#Showing the catalog until the client choose "No"
while Pedido != 'N' and Pedido != 'n':
    wrd = 'JP Engenharia'
    tracos(wrd)
    #Header with available service options of the company
    X = int(input('Choose your service:\n1.Projects\n2.Consulting\n3.Laboratory Tests\n4.Courses\n5.Cliente Service\nPlease enter the corresponding number: '))
    print('\n')

    #Case 1: Projects
    if X == 1:
        wrd = 'The available project options are: '
        tracos(wrd)
        Projetos = ['Structural','Architectural','Plumbing','Electrical','Firefighting','Accessibility']
        PrecosP = [3000,2000,1500,1000,800,500]

        for i in range(1,7):
            projeto = f"{i}.{Projetos[i-1]}".ljust(40)
            precop = f"R$ {PrecosP[i-1]:.2f}"
            print(f"{projeto} {precop}")
        
        print('\n')
        P = int(input('Please enter the corresponding number: '))

        if P != 7:
            Qtdp = int(input(f"You've added {Projetos[P-1]} at a cost of R$ {PrecosP[P-1]:.2f} per unit. How many units do you want? "))
            Comanda_Projeto = PrecosP[P-1] * Qtdp
            Cliente.append(Comanda_Projeto)
            Produtos.append(Projetos[P-1])
            Valor.append(PrecosP[P-1])
            Cont = Cont + 1
        
        Pedido = str(input('Do you wish to continue (Y/N)? '))
        
    #Case 2: Consulting
    if X ==  2:
        wrd = 'The available consulting options are: '
        tracos(wrd)
        Consultoria = ['Project Feasibility','Risks and Safety','Energy Efficiency','Environmental Responsibility','Standards and Technical Regulations']
        PrecosC = [1000,800,750,500,300]

        for i in range(1,6):
            consultoria = f"{i}.{Consultoria[i-1]}".ljust(40)
            precoc = f"R$ {PrecosC[i-1]:.2f}"
            print(f"{consultoria} {precoc}")
        
        print('\n')
        C = int(input('Please enter the corresponding number: '))

        if C != 6:
            Qtdc = int(input(f"You've added {Consultoria[C-1]} at a cost of R$ {PrecosC[C-1]:.2f} per unit. How many units do you want? "))
            Comanda_Consultoria = PrecosC[C-1] * Qtdc
            Cliente.append(Comanda_Consultoria)
            Produtos.append(Consultoria[C-1])
            Valor.append(PrecosC[C-1])
            Cont = Cont + 1
    
        Pedido = str(input('Do you wish to continue (Y/N)? '))
        
    #Case 3: Laboratory Tests
    if X ==  3:
        wrd = 'The available laboratory test options are: '
        tracos(wrd)
        Laboratorio = ['Specific Gravity of Aggregates','Particle Size Distribution','Compressive Strength','Proctor Compaction','California Bearing Ratio','Atterberg Limits']
        PrecosL = [1000,800,600,500,400,300]

        for i in range(1,7):
            laboratorio = f"{i}.{Laboratorio[i-1]}".ljust(40)
            precol = f"R$ {PrecosL[i-1]:.2f}"
            print(f"{laboratorio} {precol}")

        print('\n')
        L = int(input('Please enter the corresponding number: '))

        if L != 7:
            Qtdl = int(input(f"You've added {Laboratorio[L-1]} at a cost of R$ {PrecosL[L-1]:.2f} per unit. How many units do you want? "))
            Comanda_Laboratorio = PrecosL[L-1] * Qtdl
            Cliente.append(Comanda_Laboratorio)
            Produtos.append(Laboratorio[L-1])
            Valor.append(PrecosL[L-1])
            Cont = Cont + 1

        Pedido = str(input('Do you wish to continue (Y/N)? '))
        
    #Caso 4: Courses
    if X ==  4:
        wrd = 'The available course options are: '
        tracos(wrd)
        Cursos = ['Structural Calculation','Slope Stability','Python for Engineers','Power BI for Engineers','Excel for Engineers','Civil 3D']
        PrecosK = [1500,1200,1000,850,700,500]

        for i in range(1,7):
            cursos = f"{i}.{Cursos[i-1]}".ljust(40)
            precok = f"R$ {PrecosK[i-1]:.2f}"
            print(f"{cursos} {precok}")

        print('\n')
        K = int(input('Please enter the corresponding number: '))

        if K != 7:
            Qtdk = int(input(f"You've added {Cursos[K-1]} at a cost of R$ {PrecosK[K-1]:.2f} per unit. How many units do you want? "))
            Comanda_Cursos = PrecosK[K-1] * Qtdk
            Cliente.append(Comanda_Cursos)
            Produtos.append(Cursos[K-1])
            Valor.append(PrecosK[K-1])
            Cont = Cont + 1
       
        Pedido = str(input('Do you wish to continue (Y/N)? '))
        
    #Caso 5: Cliente Service
    if X ==  5:
        print('You have contacted the customer service. Please describe your issue, and we will get back to your email as soon as possible.')
        reclame = str(input('''Enter your complaint: '''))
        
        #Definition of a function that sends an email to the customer support department (CSD)
        def reclame_email():
            corpo_email = f""" 
            <p>Client: {nome}\n</p>
            <p>Telephone number: {telefone}\n</p>
            <p>Contact email: {gmail}\n\n\n</p>
            <p>Complaint: {reclame}\n\n\n</p>
            <p>Att,\n\n</p>
            <p>J. Pedro.</p>               
            """
            msg = email.Message()
            msg["Subject"] = f"Complaint - Client {nome}"
            msg["From"] = "joaopp.eng@gmail.com"
            msg["To"] = "RH.JPEngenharia@gmail.com"
            password = "txdwwuoyfpusutoj"
            msg.add_header('Content-type', 'text/html')
            msg.set_payload(corpo_email)
            
            s = smtp.SMTP('smtp.gmail.com', 587)
            s.starttls()
            s.login(msg["From"], password)
            s.sendmail(msg["From"], msg["To"], msg.as_string().encode('utf-8'))

        reclame_email()    
        print('We apologize for the inconvenience. Your complaint has been sent to the relevant department.')
      
print('\n')
Soma = 0

#Calculation of the budget value
for i in range(0,Cont-1):
    Soma = Soma + Cliente[i]

print('The total value of your budget is R$ {:.2f}\n'.format(Soma))

CPF = str(input('CPF (Y/N)? '))

#Printing of a fiscal receipt with the option of CPF       
if CPF == 'Y' or CPF == 'y':
    N = str(input('Enter your CPF: '))
    wrd = 'FISCAL RECEIPT'
    tracos(wrd)
    print(f'\nClient CPF: {N}\n')
    p = f"{'SERVICES'}".ljust(40)
    v = f"{'PRICE'}"
    wrd = f"{p} {v}"
    tracos(wrd)

    for i in range(1,Cont):
        produtos = f"{i}.{Produtos[i-1]}".ljust(40)
        valor = f"R$ {Valor[i-1]:.2f}"
        print(f"{produtos} {valor}")
    
    print('\n')
    t = f"{'TOTAL'}".ljust(40)
    s = float(f"{Soma}")
    wrd = f'{t} R$ {s:.2f}'
    tracos(wrd)

else:
    wrd = 'FISCAL RECEIPT'
    tracos(wrd)
    p = f"{'SERVICES'}".ljust(40)
    v = f"{'PRICE'}"
    wrd = f"{p} {v}"
    tracos(wrd)
    

    for i in range(1,Cont):
        produtos = f"{i}.{Produtos[i-1]}".ljust(40)
        valor = f"R$ {Valor[i-1]:.2f}"
        print(f"{produtos} {valor}")
    
    print(f'TOTAL  R$ {Soma:.2f}'.ljust(40))

#Definition of a function that sends an email to the client with the budget value
def enviar_email():
    corpo_email = f""" 
    <p>Hi, {nome}!</p>
    <p>Thank you for choosing us. The value of your budget was R$ {Soma:.2f}.</p>
    <p>For more information, contact us on our WhatsApp:</p>
    <p>XX XXXXXXXXXXX</p>
    <p>Come back anytime!</p>
    """
    msg = email.Message()
    msg["Subject"] = "Budget - JP Engenharia"
    msg["From"] = "joaopp.eng@gmail.com"
    msg["To"] = f"{gmail}" 
    password = "txdwwuoyfpusutoj"
    msg.add_header('Content-type', 'text/html')
    msg.set_payload(corpo_email)
    
    s = smtp.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(msg["From"], password)
    s.sendmail(msg["From"], msg["To"], msg.as_string().encode('utf-8'))
    print('\n')
    print('"Thank you for your trust. A summary of your budget has been sent to your email.".')

#Sending e-mail
enviar_email()

#Script termination command
input("Press 'Enter' to exit.")


    


    
    




