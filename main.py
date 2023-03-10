import tkinter as tk
from tkinter import ttk

#create root app (window)
rootApp = tk.Tk()
rootApp.title("Ottoshop")
rootApp.geometry("300x450")

invoiceDialogObj = None

def showInvoiceDialog():
    from invoice import invoiceDialog
    global invoiceDialogObj
    invoiceDialogObj = invoiceDialog(rootApp)
    invoiceDialogObj.renderDialog()

financialDialogObj = None

def showFinancialDialog():
    from financialreport import FinancialDialog
    global financialDialogObj
    financialDialogObj = FinancialDialog(rootApp)
    financialDialogObj.showDialog()

addCompanyDialogObj = None

def showAddCompanyDialog():
    from addcompany import addCompanyDialog
    global addCompanyDialogObj
    addCompanyDialogObj = addCompanyDialog(rootApp)
    addCompanyDialogObj.showAddCompanyDialog()

addClientDialogObj = None

def showAddClientDialog():
    from addclient import addClientDialog
    global addClientDialogObj
    addClientDialogObj = addClientDialog(rootApp)
    addClientDialogObj.renderDialog()

addProductDialogObj = None

def showAddProductDialog():
    from addproduct import AddProductDialog
    global addProductDialogObj
    addProductDialogObj = AddProductDialog(rootApp)
    addProductDialogObj.showAddProductDialog()

changeProductDialogObj = None

def showChangeProductDialog():
    from changeproduct import ChangeProductDialog
    global changeProductDialogObj
    changeProductDialogObj = ChangeProductDialog(rootApp)
    changeProductDialogObj.render_dialog()

barCodeDialogObj = None

def showBarCodeDialog():
    from barcode import BarCodeDialog
    global barCodeDialogObj
    barCodeDialogObj = BarCodeDialog(rootApp)
    barCodeDialogObj.renderDialog()

declarationDialogObj = None

def showDeclarationDialog():
    from printdeclaration import PrintDeclaration
    global declarationDialogObj
    declarationDialogObj = PrintDeclaration(rootApp)
    declarationDialogObj.render_dialog()

def closeApp():
    rootApp.quit()                                                               
#change window icon
icon = tk.PhotoImage(file='./content/logo.png')
rootApp.wm_iconphoto(True, icon)
# #create each button on starting form
ttk.Button(rootApp, text='Fakturisanje', command=showInvoiceDialog, width=20).pack(padx=30, pady=10)
ttk.Button(rootApp, text='Finansijski Izvestaj', command=showFinancialDialog, width=20).pack(padx=30, pady=10)
ttk.Button(rootApp, text='Bar Kodovi', command=showBarCodeDialog, width=20).pack(padx=30, pady=10)
ttk.Button(rootApp, text='Etikete', command=showDeclarationDialog, width=20).pack(padx=30, pady=10)
ttk.Button(rootApp, text='Dodaj Firmu', command=showAddCompanyDialog, width=20).pack(padx=30, pady=10)
ttk.Button(rootApp, text='Dodaj Klijenta', command=showAddClientDialog, width=20).pack(padx=30, pady=10)
ttk.Button(rootApp, text='Dodaj Proizvod', command=showAddProductDialog, width=20).pack(padx=30, pady=10)
ttk.Button(rootApp, text='Izmeni Proizvod', command=showChangeProductDialog, width=20).pack(padx=30, pady=10)
ttk.Button(rootApp, text='Izadji', command=closeApp, width=10).pack(padx=30, pady=30)

# #initiate main form
rootApp.mainloop()