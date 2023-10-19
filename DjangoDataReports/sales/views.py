from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import DetailView
from .models import Sale
from.forms import SalesSearchForm
from .utils import get_salesman_from_id, get_customer_from_id

import pandas as pd

# Create your views here.
def home(request):
    sales_df = None
    position_df = None
    merge_df = None
    group_df = None
    form = SalesSearchForm(request.POST or None)
    if request.method == 'POST':
        date_from = request.POST.get('date_from')
        date_to = request.POST.get('date_to')
        chart_type = request.POST.get('chart_type')
        sales_qs = Sale.objects.filter(created__date__lte = date_to,created__date__gte = date_from)
        if(len(sales_qs)>0):
            df = pd.DataFrame(sales_qs.values())   # with table header 
            df['customer_id'] = df['customer_id'].apply(get_customer_from_id)
            df['salesman_id'] =  df['salesman_id'].apply(get_salesman_from_id)
            df.rename({'customer_id':"customer","salesman_id":"salesman","id":"sale_id"},axis=1,inplace=True)
            df['created']= df['created'].apply(lambda x:x.strftime('%d-%m-%Y') )
            df['updated']= df['updated'].apply(lambda x:x.strftime('%d-%m-%Y') )
           
            
            positions_data = []
            for sale in sales_qs:
                for pos in sale.get_positions():
                    obj = {
                        'position_id': pos.id,
                        'product': pos.product.name,
                        'quantity': pos.quantity,
                        'price': pos.price,
                        'sale_id': pos.get_sale_id(),
                        # 'sale_id': pos.sale.first().id,
                    }
                    positions_data.append(obj)
            df1 = pd.DataFrame(positions_data)
            df3 = pd.merge(df,df1,on='sale_id')
            df4 = df3.groupby('transaction_id',as_index=False)['price'].agg('sum')
            sales_df = df.to_html(index=False)
            position_df = df1.to_html(index=False)
            merge_df = df3.to_html(index=False)
            group_df = df4.to_html()
            
           
    # return render(request=request,template_name='sales/home.html',context={'form':form,'sales_df':sales_df,'position_df':position_df})
    return render(request=request,template_name='sales/home.html',context={'form':form,'sales_df':sales_df,'position_df':position_df,'merge_df':merge_df,'group_df':group_df})


class SalesListView(ListView):
    template_name = 'sales/main.html'
    model = Sale
    context_object_name = "sales_list"

class SalesDetailView(DetailView):
    model = Sale
    template_name = 'sales/detail.html'
    
    