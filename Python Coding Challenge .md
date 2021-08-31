```python
#Python Coding challenge
#Loading Libraries
#numpy

import numpy as np
```


```python
#pandas

import pandas as pd
```


```python
#json

import json
```


```python
#Reading Dataset from URL
#Loading the json file as a dataframe

df = pd.read_json("https://raw.githubusercontent.com/onaio/ona-tech/master/data/water_points.json")
```


```python
print(df)
```

        water_pay                 respondent research_asst_name water_used_season  \
    0          no                  community    Haruna Mohammed        year_round   
    1          no                  community     Haruna Mohmmed        year_round   
    2          no                  community    Haruna Mohammed        year_round   
    3          no                  community    Haruna Mohammed        year_round   
    4          no                  community    Haruna Mohammed        year_round   
    ..        ...                        ...                ...               ...   
    707        no                  community         Emmanuel y        year_round   
    708        no  local_authority community         Emmanuel y        year_round   
    709        no  local_authority community         Emmanuel y        year_round   
    710        no                  community          abu seidu        year_round   
    711        no                  community                 Sa        year_round   
    
        _bamboo_dataset_id _deleted_at water_point_condition     _xform_id_string  \
    0                              NaT           functioning  _08_Water_points_CV   
    1                              NaT           functioning  _08_Water_points_CV   
    2                              NaT           functioning  _08_Water_points_CV   
    3                              NaT           functioning  _08_Water_points_CV   
    4                              NaT           functioning  _08_Water_points_CV   
    ..                 ...         ...                   ...                  ...   
    707                            NaT           functioning  _08_Water_points_CV   
    708                            NaT                broken  _08_Water_points_CV   
    709                            NaT                broken  _08_Water_points_CV   
    710                            NaT           functioning  _08_Water_points_CV   
    711                            NaT           functioning  _08_Water_points_CV   
    
        other_point_1km                                 _attachments  ...  \
    0                no  [north_ghana/attachments/1351696546452.jpg]  ...   
    1               yes  [north_ghana/attachments/1351701849971.jpg]  ...   
    2               yes  [north_ghana/attachments/1351702462336.jpg]  ...   
    3               yes  [north_ghana/attachments/1351702971561.jpg]  ...   
    4               yes  [north_ghana/attachments/1351703622326.jpg]  ...   
    ..              ...                                          ...  ...   
    707              no  [north_ghana/attachments/1358151218133.jpg]  ...   
    708             yes  [north_ghana/attachments/1358081512606.jpg]  ...   
    709             yes  [north_ghana/attachments/1358081512606.jpg]  ...   
    710              no  [north_ghana/attachments/1358175596571.jpg]  ...   
    711             yes  [north_ghana/attachments/1355488003808.jpg]  ...   
    
        animal_point water_mechanism_plate water_lift_mechanism_type    road_type  \
    0            yes                   NaN                       NaN          NaN   
    1            yes                    no              manual_power       gravel   
    2            yes                    no              manual_power        paved   
    3            yes                    no              manual_power        paved   
    4            yes                    no              manual_power        paved   
    ..           ...                   ...                       ...          ...   
    707          yes                    no                 hand_pump          NaN   
    708          yes                    no                 hand_pump          NaN   
    709          yes                    no                 hand_pump          NaN   
    710          yes                    no                 hand_pump          NaN   
    711          yes                    no              manual_power  gravel dirt   
    
        water_mechanism_plate_units water_mechanism_plate_no  \
    0                           NaN                      NaN   
    1                           NaN                      NaN   
    2                           NaN                      NaN   
    3                           NaN                      NaN   
    4                           NaN                      NaN   
    ..                          ...                      ...   
    707                         NaN                      NaN   
    708                         NaN                      NaN   
    709                         NaN                      NaN   
    710                         NaN                      NaN   
    711                         NaN                      NaN   
    
        water_not_functioning water_source_type_other     simserial  subscriberid  
    0                     NaN                     NaN           NaN           NaN  
    1                     NaN                     NaN           NaN           NaN  
    2                     NaN                     NaN           NaN           NaN  
    3                     NaN                     NaN           NaN           NaN  
    4                     NaN                     NaN           NaN           NaN  
    ..                    ...                     ...           ...           ...  
    707                   NaN                     NaN           NaN           NaN  
    708                   NaN                     NaN           NaN           NaN  
    709                   NaN                     NaN           NaN           NaN  
    710                   NaN                     NaN  8.923301e+18  6.200101e+14  
    711                   NaN                     NaN           NaN           NaN  
    
    [712 rows x 48 columns]
    


```python
#The defined variables of interest

module = df[["communities_villages", "water_functioning"]]
```


```python
print(module)
```

        communities_villages water_functioning
    0              Gumaryili               yes
    1              Selinvoya               yes
    2              Selinvoya               yes
    3              Selinvoya               yes
    4              Selinvoya               yes
    ..                   ...               ...
    707                 Suik               yes
    708              Vundema               yes
    709              Vundema               yes
    710             Jiniensa               yes
    711                Jagsa               yes
    
    [712 rows x 2 columns]
    


```python
#The number of water points that are functional

moduleA = df.groupby(['water_functioning'])['communities_villages'].count()
```


```python
print(moduleA)
```

    water_functioning
    na_dn      2
    no        87
    yes      623
    Name: communities_villages, dtype: int64
    


```python
#The number of water points per community

moduleB = df.groupby(['communities_villages'])['water_functioning'].count()
```


```python
print(moduleB)
```

    communities_villages
    Abanyeri        4
    Akpari-yeri     3
    Alavanyo        3
    Arigu          12
    Badomsa        27
                   ..
    Zogsa           6
    Zua            28
    Zuedema        18
    Zukpeni         6
    Zundem         30
    Name: water_functioning, Length: 65, dtype: int64
    


```python
#The rank of each community by the percentage of broken water points

moduleC = df[["communities_villages", "water_point_condition"]]
```


```python
counts = moduleC.value_counts()
```


```python
print(counts)
```

    communities_villages  water_point_condition
    Kpatarigu             functioning              43
    Jagsa                 functioning              34
    Nayoku                functioning              29
    Zundem                functioning              29
    Nabulugu              functioning              29
                                                   ..
    Luisa                 broken                    1
    Nabulugu              abandoned                 1
                          newly_constructed         1
    Nyandema              newly_constructed         1
    Zundem                under_construction        1
    Length: 134, dtype: int64
    


```python
percent = moduleC.value_counts(normalize = True)
```


```python
print(percent)
```

    communities_villages  water_point_condition
    Kpatarigu             functioning              0.060393
    Jagsa                 functioning              0.047753
    Nayoku                functioning              0.040730
    Zundem                functioning              0.040730
    Nabulugu              functioning              0.040730
                                                     ...   
    Luisa                 broken                   0.001404
    Nabulugu              abandoned                0.001404
                          newly_constructed        0.001404
    Nyandema              newly_constructed        0.001404
    Zundem                under_construction       0.001404
    Length: 134, dtype: float64
    


```python
percent100 = moduleC.value_counts(normalize = True).mul(100).round(1).astype(str) + '%'
```


```python
print(percent100)
```

    communities_villages  water_point_condition
    Kpatarigu             functioning              6.0%
    Jagsa                 functioning              4.8%
    Nayoku                functioning              4.1%
    Zundem                functioning              4.1%
    Nabulugu              functioning              4.1%
                                                   ... 
    Luisa                 broken                   0.1%
    Nabulugu              abandoned                0.1%
                          newly_constructed        0.1%
    Nyandema              newly_constructed        0.1%
    Zundem                under_construction       0.1%
    Length: 134, dtype: object
    


```python
Final_module = f'{moduleA}{moduleB}{percent100}'
```


```python
print(Final_module)
```

    water_functioning
    na_dn      2
    no        87
    yes      623
    Name: communities_villages, dtype: int64communities_villages
    Abanyeri        4
    Akpari-yeri     3
    Alavanyo        3
    Arigu          12
    Badomsa        27
                   ..
    Zogsa           6
    Zua            28
    Zuedema        18
    Zukpeni         6
    Zundem         30
    Name: water_functioning, Length: 65, dtype: int64communities_villages  water_point_condition
    Kpatarigu             functioning              6.0%
    Jagsa                 functioning              4.8%
    Nayoku                functioning              4.1%
    Zundem                functioning              4.1%
    Nabulugu              functioning              4.1%
                                                   ... 
    Luisa                 broken                   0.1%
    Nabulugu              abandoned                0.1%
                          newly_constructed        0.1%
    Nyandema              newly_constructed        0.1%
    Zundem                under_construction       0.1%
    Length: 134, dtype: object
    


```python

```
