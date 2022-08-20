from urllib import response
from django.shortcuts import render,redirect
from django.contrib import messages
from tallyapp.models import Companies, Countries,Gst_Details,Person,Tds_Details,Features,States
from django.http import HttpResponseRedirect
from datetime import date

from datetime import timedelta
import datetime
# Create your views here.
# def base(request):
#     return render(request,'base.html')

def create(request):
    Country=Countries.objects.all()
    return render(request,'company.html',{'country':Country})

def companycreate(request):
    
    if request.method=="POST":
        name=request.POST['companyname']
        print(name)
        mailing_name=request.POST['mailing_name']
        print(mailing_name)
        address=request.POST['address']
        print(address)
        state=request.POST['state']
        print(state)
        country=request.POST['country']
        print(country)
        pincode=request.POST['pincode']
        print(pincode)
        telephone=request.POST['telephone']
        print(telephone)
        mobile=request.POST['mobile']
        print(mobile)
        fax=request.POST['fax']
        print(fax)
        email=request.POST['email1']
        print(email)
        website=request.POST['website']
        print(website)
        fin_begin=request.POST['fyear']
        print(fin_begin)
        books_begin=request.POST['byear']
        print(books_begin)
        currency_symbol=request.POST['currency']
        print(currency_symbol)
        formal_name=request.POST['formal']
        print(formal_name)
        cmp=Companies.objects.filter(name=name)
        
        out=datetime.datetime.strptime (fin_begin,'%Y-%m-%d')+timedelta (days=364) 
        print(out)
        a=out.date()
        print(a)
        if cmp:
            messages.info(request,'Company name already exists!!')
            return redirect('create')
        else:
            ctg=Companies(name=name,mailing_name=mailing_name,address=address,state=state,country=country,
                pincode=pincode,telephone=telephone,mobile=mobile,fax=fax,email=email,website=website,fin_begin=fin_begin,
                books_begin=books_begin,currency_symbol=currency_symbol,formal_name=formal_name,fin_end=a)
                
            ctg.save()
            messages.info(request,'Company created successfully(Enable the features as per your business needs)')
            return render(request,'features.html',{'ctg':ctg})
def gst_details(request,pk):
    company=Companies.objects.get(id=pk)
    return render(request,'gst_details.html',{'companies':company})
def add_gstdetails(request,pk):
    id=Companies.objects.get(id=pk)
    comp=Companies.objects.get(id=pk)
    
    if request.method=="POST":
        state=request.POST['state']
        registration_type=request.POST['registration_type']
        assessee=request.POST['assessee']
        fdate=request.POST['fdate']
        gstin=request.POST['gstin']
        periodicity=request.POST['periodicity']
        alter_gst=request.POST['alter_gst']
        tax_liabilityadvance=request.POST['tax_liabilityadvance']
        tax_liability=request.POST['tax_liability']
        gst_classifications=request.POST['gst_classifications']
        bond_details=request.POST['bond_details']
        eway_bill=request.POST['eway_bill']
        applicable_from=request.POST['applicable_from']
        treshold_limit=request.POST['treshold_limit']
        treshold_limit1=request.POST['treshold_limit1']
        intrastate=request.POST['intrastate']
        treshold_limit2=request.POST['treshold_limit2']
        print_ewaybill=request.POST['print_ewaybill']
        e_invoicing=request.POST['e_invoicing']
        gst=Gst_Details(state= state,reg_type=registration_type,assessee= assessee,app_form= fdate,gstin= gstin,gstr1= periodicity,
                        rate_details= alter_gst,advance_receipts=tax_liabilityadvance,reverse_charge=tax_liability,classifications= gst_classifications,
                        bond_details=bond_details,eway_bill= eway_bill,applicable_form=applicable_from,threshold_includes= treshold_limit,
                         threshold_limit1=treshold_limit1,intrastate=intrastate,threshold_limit2=treshold_limit2,print_eway=print_ewaybill,e_invoice= e_invoicing,company=id)
        gst.save()
        messages.info(request,'Gst details added..!!')
    return redirect(request.META.get('HTTP_REFERER'))    
def tds_deductor(request,pk):
    comp=Companies.objects.get(id=pk)
    return render(request,'tds_deductor.html',{'company':comp})
def person_details(request,pk):
    com=Companies.objects.get(id=pk)
    return render(request,'person_details.html',{'comp':com})  
def add_person(request,pk):
    id=Companies.objects.get(id=pk)
    if request.method=="POST":
        name=request.POST['name']
        fname=request.POST['fname']
        Designation=request.POST['Designation']
        pan=request.POST['pan']
        address=request.POST['address']
        bname=request.POST['bname']
        road=request.POST['road']
        area=request.POST['area']
        city=request.POST['city']
        pin=request.POST['pin']
        state=request.POST['state']
        mobile=request.POST['mobile']
        std=request.POST['std']
        telephone=request.POST['telephone']
        email=request.POST['email']
        
        person=Person(name=name,fname=fname,designation=Designation,pan=pan,flatno=address,building=bname,road=road,area=area,town=city,
                      pincode=pin,state=state,mobile=mobile,std=std,telephone=telephone,email=email,company=id)
        person.save()
        messages.info(request,'Person details added..!!')
    return redirect(request.META.get('HTTP_REFERER'))  

def add_tds(request,pk):
    id=Companies.objects.get(id=pk)
    if(request.method=="POST"):
        tan_number=request.POST['tan_number']
        tan=request.POST['tan']
        deductor=request.POST['deductor']
        branch=request.POST['branch']
        person_details=request.POST['person_details']
        exemption=request.POST['exemption']
        active_tds=request.POST['active_tds']
        tds=Tds_Details(tan_regno=tan_number,tan=tan,deductor_type=deductor,deductor_branch=branch,person_details= person_details,
                        excemption_limit=exemption,activate_tds=active_tds,company=id)
        tds.save()
        messages.info(request,'TDS details added..!!')
    return redirect(request.META.get('HTTP_REFERER'))    

def features(request,pk):
    id=Companies.objects.get(id=pk)
    # feature=Features.objects.get(company=pk)
    print(id)
    if request.method == "POST":
        maintain_accounts=request.POST['maintain_accounts']
        bill_wise_entry=request.POST['bill_wise_entry']
        cost_centres=request.POST['cost_centres']
        interest_calc=request.POST['interest_calc']
        maintain_inventory=request.POST['maintain_inventory']
        integrate_accounts=request.POST['integrate_accounts']
        multiple_price_level=request.POST['multiple_price_level']
        batches=request.POST['batches']
        expirydate_batches=request.POST['expirydate_batches']
        joborder_processing=request.POST['joborder_processing']
        cost_tracking=request.POST['cost_tracking']
        job_costing=request.POST['job_costing']
        Discount_coloumn=request.POST['Discount_coloumn']
        billed_quantity=request.POST['billed_quantity']
        gst=request.POST['gst']
        
        tds=request.POST['tds']
        tcs=request.POST['tcs']
        vat=request.POST['vat']
        excise=request.POST['excise']
        service_tax=request.POST['service_tax']
        payroll=request.POST['payroll']
        payroll_statutory=request.POST['payroll_statutory']
        multiple_address=request.POST['multiple_address']
        Modified_vouchers=request.POST['Modified_vouchers']
        feature=Features(maintain_accounts=maintain_accounts,bill_wise_entry=bill_wise_entry, cost_centres= cost_centres,interest_calc=interest_calc,
                         maintain_inventory= maintain_inventory,integrate_accounts=integrate_accounts, multiple_price_level= multiple_price_level,
                          batches= batches, expirydate_batches= expirydate_batches,joborder_processing=joborder_processing,cost_tracking= cost_tracking,
                          job_costing=job_costing,discount_invoices=Discount_coloumn,Billed_Quantity=billed_quantity,gst=gst,tds=tds,tcs=tcs,vat=vat,
                          excise=excise, servicetax=service_tax,payroll=payroll, payroll_statutory= payroll_statutory,multiple_addrss=multiple_address,
                           vouchers=Modified_vouchers,company=id)
        feature.save() 
        
        return redirect('dashboard')
    return render(request,'features.html',{'ctg':id})
def dashboard(request):
    com=Companies.objects.filter(status=True)
    
       
    comp1=Companies.objects.first()
    comp1.status=True
   
    comp1.save()
    return render(request,'dashboard.html',{'comp1':comp1,'com1':com})

def company_list(request):
    com=Companies.objects.all()
    return render(request,'company_list.html',{'comp':com})       

def select_company(request):
    comp=Companies.objects.all()
    
    return render(request,'select_company.html',{'comp1':comp})

def dash_board(request,pk):
    comp=Companies.objects.get(id=pk)
    comp.status=True
    comp.save()
    com=Companies.objects.filter(status=True)  
    return render(request,'dashboard.html',{'comp1':comp,'com1':com})

def alter_company(request):
    comp=Companies.objects.all()
    return render(request,'alter_company.html',{'comp1':comp})

def edit_page(request,pk):
    country=Countries.objects.all()
    com=Companies.objects.get(id=pk)
    return render(request,'edit_company.html',{'com':com,'country':country})

def edit_companydetails(request,pk):
    com=Companies.objects.get(id=pk)
    if request.method=="POST":
        com.name=request.POST['companyname']
       
        com.mailing_name=request.POST['mailing_name']
       
        com.address=request.POST['address']
        
        com.state=request.POST['state']
      
        com.country=request.POST['country']
       
        com.pincode=request.POST['pincode']
        
        com.telephone=request.POST['telephone']
        
        com.mobile=request.POST['mobile']
        
        com.fax=request.POST['fax']
        
        com.email=request.POST['email']
       
        com.website=request.POST['website']
        
        com.fin_begin=request.POST['fyear']
        com.books_begin=request.POST['byear']
       
        com.currency_symbol=request.POST['currency']
        
        com.formal_name=request.POST['formal']
        com.save()
        return redirect('dashboard')
        
def change_company(request):
    com=Companies.objects.filter(status=True) 
    return render(request,'change_company.html',{'com':com})        

def shut_company(request):
    com=Companies.objects.filter(status=True) 
    return render(request,'shut_company.html',{'com':com})

def shut(request,pk):
    com=Companies.objects.get(id=pk)
    com.status=False
    com.save()
    comp1=Companies.objects.first()
    com=Companies.objects.filter(status=True) 
    return render(request,'dashboard.html',{'com1':com,'comp1':comp1})

def date_change(request):
    return render(request,'date.html')

def print_config(request):
    return render(request,'print_config.html')

def add_country(request):
    if request.method=="POST":
        print("a")
        country=request.POST['country_name']
        print(country)
        countries=Countries(name=country)
        countries.save()
        return redirect('create') 
    
def download(request):
    return response

def addstates(request):
    
    state=States.objects.filter(country_id=id)
    print(state)
    return render(request,'company.html',{'state':state})

def state_country(request):
    return render(request,'state_country.html')

def load_cities(request):
    country_id=request.POST['country_id']
    states=States.objects.filter(country_id=country_id)
    return render(request,'company.html',{'states':states})

def  edit_features(request,pk):
    id=Companies.objects.get(id=pk)
    # feature=Features.objects.get(company=pk)
    print(id)
    if request.method == "POST":
        maintain_accounts=request.POST['maintain_accounts']
        bill_wise_entry=request.POST['bill_wise_entry']
        cost_centres=request.POST['cost_centres']
        interest_calc=request.POST['interest_calc']
        maintain_inventory=request.POST['maintain_inventory']
        integrate_accounts=request.POST['integrate_accounts']
        multiple_price_level=request.POST['multiple_price_level']
        batches=request.POST['batches']
        expirydate_batches=request.POST['expirydate_batches']
        joborder_processing=request.POST['joborder_processing']
        cost_tracking=request.POST['cost_tracking']
        job_costing=request.POST['job_costing']
        Discount_coloumn=request.POST['Discount_coloumn']
        billed_quantity=request.POST['billed_quantity']
        gst=request.POST['gst']
        
        tds=request.POST['tds']
        tcs=request.POST['tcs']
        vat=request.POST['vat']
        excise=request.POST['excise']
        service_tax=request.POST['service_tax']
        payroll=request.POST['payroll']
        payroll_statutory=request.POST['payroll_statutory']
        multiple_address=request.POST['multiple_address']
        Modified_vouchers=request.POST['Modified_vouchers']
        feature=Features(maintain_accounts=maintain_accounts,bill_wise_entry=bill_wise_entry, cost_centres= cost_centres,interest_calc=interest_calc,
                         maintain_inventory= maintain_inventory,integrate_accounts=integrate_accounts, multiple_price_level= multiple_price_level,
                          batches= batches, expirydate_batches= expirydate_batches,joborder_processing=joborder_processing,cost_tracking= cost_tracking,
                          job_costing=job_costing,discount_invoices=Discount_coloumn,Billed_Quantity=billed_quantity,gst=gst,tds=tds,tcs=tcs,vat=vat,
                          excise=excise, servicetax=service_tax,payroll=payroll, payroll_statutory= payroll_statutory,multiple_addrss=multiple_address,
                           vouchers=Modified_vouchers,company=id)
        feature.save() 
        
        return redirect('dashboard')
    return render(request,'edit_features.html',{'ctg':id})

def edit_gst_details(request,pk):
    id=Companies.objects.get(id=pk)
    comp=Companies.objects.get(id=pk)
    gst=Gst_Details.objects.get(company_id=pk)
    
    return render(request,'edit_gst_details.html',{'gst':gst,'comp':comp})
    
def add_newgstdetails(request,pk):
    gst=Gst_Details.objects.get(company_id=pk)
    if request.method=="POST":
        gst.state=request.POST['state']
        gst.registration_type=request.POST['registration_type']
        gst.assessee=request.POST['assessee']
        gst.fdate=request.POST['fdate']
        gst.gstin=request.POST['gstin']
        gst.periodicity=request.POST['periodicity']
        gst.alter_gst=request.POST['alter_gst']
        gst.tax_liabilityadvance=request.POST['tax_liabilityadvance']
        gst.tax_liability=request.POST['tax_liability']
        gst.gst_classifications=request.POST['gst_classifications']
        gst.bond_details=request.POST['bond_details']
        gst.eway_bill=request.POST['eway_bill']
        gst.applicable_from=request.POST['applicable_from']
        gst.treshold_limit=request.POST['treshold_limit']
        gst.treshold_limit1=request.POST['treshold_limit1']
        gst.intrastate=request.POST['intrastate']
        gst.treshold_limit2=request.POST['treshold_limit2']
        gst.print_ewaybill=request.POST['print_ewaybill']
        gst.e_invoicing=request.POST['e_invoicing']
       
        gst.save()
        messages.info(request,'Gst details updated..!!')
    return redirect(request.META.get('HTTP_REFERER'))

def edit_tds_deductor(request,pk):
    id=Companies.objects.get(id=pk)
    comp=Companies.objects.get(id=pk)
    tds=Tds_Details.objects.get(company_id=pk)
    
    return render(request,'edit_tds_details.html',{'tds':tds,'comp':comp})
def add_newtdsdetails(request,pk):
    tds=Tds_Details.objects.get(company_id=pk)
    if(request.method=="POST"):
        tds.tan_number=request.POST['tan_number']
        tds.tan=request.POST['tan']
        tds.deductor=request.POST['deductor']
        tds.branch=request.POST['branch']
        tds.person_details=request.POST['person_details']
        tds.exemption=request.POST['exemption']
        tds.active_tds=request.POST['active_tds']
        
        tds.save()
        messages.info(request,'TDS details updated..!!')
    return redirect(request.META.get('HTTP_REFERER'))   
def edit_person_details(request,pk):
    id=Companies.objects.get(id=pk)
    comp=Companies.objects.get(id=pk)
    person=Person.objects.get(company_id=pk)
    
    return render(request,'editperson_details.html',{'person':person,'comp':comp})
def add_newpersondetails(request,pk):
    person=Person.objects.get(company_id=pk)
    if request.method=="POST":
        person.name=request.POST['name']
        person.fname=request.POST['fname']
        person.Designation=request.POST['Designation']
        person.pan=request.POST['pan']
        person.address=request.POST['address']
        person.bname=request.POST['bname']
        person.road=request.POST['road']
        person.area=request.POST['area']
        person.city=request.POST['city']
        person.pin=request.POST['pin']
        person.state=request.POST['state']
        person.mobile=request.POST['mobile']
        person.std=request.POST['std']
        person.telephone=request.POST['telephone']
        person.email=request.POST['email']
        
       
        person.save()
        messages.info(request,'Person details Updated..!!')
    return redirect(request.META.get('HTTP_REFERER'))  
    
    