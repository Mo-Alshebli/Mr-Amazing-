import matplotlib
import skfuzzy as fuzz
import numpy as np
import matplotlib.pyplot as plt
from tkinter import *
fram = Tk()

# Fuzzification
x_MAP = np.arange(0, 201, 1)
x_HUO = np.arange(0, 201, 1)
x_IFR = np.arange(0, 2001, 1)

low_MAP = fuzz.trapmf(x_MAP, [0, 0, 55, 75])
normal_MAP = fuzz.trapmf(x_MAP, [55, 75, 100, 120])
high_MAP = fuzz.trapmf(x_MAP, [100, 120, 200, 200])
lwo_HUO = fuzz.trapmf(x_HUO, [0, 0, 30, 40])
normal_HUO = fuzz.trapmf(x_HUO, [30, 40, 100, 125])
high_HUO = fuzz.trapmf(x_HUO, [100, 125, 200, 200])

low_IFR = fuzz.trapmf(x_IFR, [0, 0, 60, 100])
maintain_IFR = fuzz.trapmf(x_IFR, [60, 100, 200, 400])
modrate_IFR = fuzz.trapmf(x_IFR, [200, 400, 600, 800])
high_IFR = fuzz.trapmf(x_IFR, [600, 800, 1000, 1500])
vereyhigh_IFR = fuzz.trapmf(x_IFR, [1000, 1500, 2000, 2000])

fig, (ax0, ax1, ax2) = plt.subplots(nrows=3, figsize=(8, 9))
ax0.plot(x_MAP, low_MAP, 'b', linewidth=1.5, label='LOW')
ax0.plot(x_MAP, normal_MAP, 'y', linewidth=1.5, label='NORMAL')
ax0.plot(x_MAP, high_MAP, 'r', linewidth=1.5, label='HIGH')
ax0.set_title = ('MEAN ARTERIAL BLOOD PRESSURE')
ax0.legend()

ax1.plot(x_HUO, lwo_HUO, 'b', linewidth=1.5, label='LOW')
ax1.plot(x_HUO, normal_HUO, 'y', linewidth=1.5, label='NORMAL')
ax1.plot(x_HUO, high_HUO, 'r', linewidth=1.5, label='HIGH')
ax1.set_title = ('HOURLY  URINE OUTPUT')
ax1.legend()

ax2.plot(x_IFR, low_IFR, 'b', linewidth=1.5, label='LOW')
ax2.plot(x_IFR, maintain_IFR, 'y', linewidth=1.5, label='MAINTAIN')
ax2.plot(x_IFR, modrate_IFR, 'r', linewidth=1.5, label='MODRATE')
ax2.plot(x_IFR, high_IFR, 'c', linewidth=1.5, label='HIGH')
ax2.plot(x_IFR, vereyhigh_IFR, 'm', linewidth=1.5, label='VEREYHIGH')
ax2.set_title = ('INTRAVENOUS FLUID RATE')
ax2.legend()

for ax in (ax0, ax1, ax2):
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()

plt.tight_layout()
# plt.show()


# Rule Evaluation
fram.geometry("900x350")
fram.resizable(False, False)
img = PhotoImage(file='imgs.png')
Label(fram, image=img).place(x=0, y=0)
l1 = Label(fram,bg="#06F7AF", text="Enter ARTERIAL BLOOD PRESSURE : ")
fram.title("Medical Decision Making in the Intensive Care Unit")
l1.place(x=50, y=50)
E1 = Entry(fram,bd="4",justify='center')
E1.place(x=250, y=50)

l2 = Label(fram,bg="#06F7AF", text="Enter Urine Output : ")
l2.place(x=50, y=80)
E2 = Entry(fram,bd="4",justify='center')
E2.place(x=250, y=85)
l4 = Label(fram,bg="#06F7AF", text="The result is  : ")
l4.place(x=50, y=110)


def g():
    while True:
        try:
            num = E1.get()
            blood_pressure = int(num)

            if 0 <= blood_pressure <= 200:
                MAP_lo = fuzz.interp_membership(x_MAP, low_MAP, blood_pressure)
                MAP_norm = fuzz.interp_membership(x_MAP, normal_MAP, blood_pressure)
                MAP_hi = fuzz.interp_membership(x_MAP, high_MAP, blood_pressure)
                break
        except BaseException:
            print("ERORR DAGREE FOR Mean Arterial Blood Pressure ENTER DAGREE AGINE FROM 0 TO 200 : ")

    while True:
        try:
            num2 = E2.get()
            urine_output = int(num2)
            if 0 <= urine_output <= 200:
                HOU_lo = fuzz.interp_membership(x_HUO, lwo_HUO, urine_output)
                HOU_norm = fuzz.interp_membership(x_HUO, normal_HUO, urine_output)
                HOU_hi = fuzz.interp_membership(x_HUO, high_HUO, urine_output)
                break
        except BaseException:
            print("erorr")

    # Rule 1 = if MAP is low and HUO is low, then IFR is very high
    active_rule1 = np.fmin(MAP_lo, HOU_lo)
    # Rule 2 = if MAP is low and HUO is normal, then IFR is high
    active_rule2 = np.fmin(MAP_lo, HOU_norm)
    # Rule 3 = if MAP is low and HUO is high, then IFR is moderate
    active_rule3 = np.fmin(MAP_lo, HOU_hi)
    # Rule 4 = if MAP is normal and HUO is low, then IFR is moderate
    active_rule4 = np.fmin(MAP_norm, HOU_lo)
    # Rule 5 = if MAP is normal and HUO is normal, then IFR is mantain
    active_rule5 = np.fmin(MAP_norm, HOU_norm)
    # Rule 6 = if MAP is normal and HUO is high, then IFR is mantain
    active_rule6 = np.fmin(MAP_norm, HOU_hi)
    # Rule 7 = if MAP is high and HUO is low, then IFR is low
    active_rule7 = np.fmin(MAP_hi, HOU_lo)
    # Rule 8 = if MAP is high and HUO is normal, then IFR is low
    active_rule8 = np.fmin(MAP_hi, HOU_norm)
    # Rule 9 = if MAP is high and HUO is high, then IFR is low
    active_rule9 = np.fmin(MAP_hi, HOU_hi)

    IFR_activation_vereyhigh = np.fmin(active_rule1, vereyhigh_IFR)
    IFR_activation_high = np.fmin(active_rule2, high_IFR)
    IFR_activation_moderate = np.fmin(active_rule3, modrate_IFR)

    IFR_activation2_moderate2 = np.fmin(active_rule4, modrate_IFR)
    IFR_activation2_maintain = np.fmin(active_rule5, maintain_IFR)
    IFR_activation2_maintain2 = np.fmin(active_rule6, maintain_IFR)

    IFR_activation3_low = np.fmin(active_rule7, low_IFR)
    IFR_activation3_low2 = np.fmin(active_rule8, low_IFR)
    IFR_activation3_low3 = np.fmin(active_rule9, low_IFR)

    IFR0 = np.zeros_like(x_IFR)
    fkk, (ax0, ax1, ax2) = plt.subplots(nrows=3, figsize=(8, 9))
    ax0.fill_between(x_IFR, IFR0, IFR_activation_vereyhigh, facecolor='b')
    ax0.plot(x_IFR, vereyhigh_IFR, 'b', linewidth=1.5, label='very high')
    ax0.fill_between(x_IFR, IFR0, IFR_activation_high, facecolor='y')
    ax0.plot(x_IFR, high_IFR, 'y', linewidth=1.5, label='high')
    ax0.fill_between(x_IFR, IFR0, IFR_activation_moderate, facecolor='r')
    ax0.plot(x_IFR, modrate_IFR, 'r', linewidth=1.5, label='moderate')
    ax0.set_title('Output membership (IFR very high, high & moderate )')
    ax0.legend()

    ax1.fill_between(x_IFR, IFR0, IFR_activation2_moderate2, facecolor='b')
    ax1.plot(x_IFR, modrate_IFR, 'b', linewidth=0.5, label='moderate2', )
    ax1.fill_between(x_IFR, IFR0, IFR_activation2_maintain, facecolor='y')
    ax1.plot(x_IFR, maintain_IFR, 'y', linewidth=0.5, label='mantain1')
    ax1.fill_between(x_IFR, IFR0, IFR_activation2_maintain2, facecolor='r')
    ax1.plot(x_IFR, maintain_IFR, 'r', linewidth=0.5, label='mantain2')
    ax1.set_title('Output membership (IFR moderate & 2 IFR mantain)')
    ax1.legend()

    ax2.fill_between(x_IFR, IFR0, IFR_activation3_low, facecolor='b')
    ax2.plot(x_IFR, low_IFR, 'b', linewidth=0.5, label='low1')
    ax2.fill_between(x_IFR, IFR0, IFR_activation3_low2, facecolor='y')
    ax2.plot(x_IFR, low_IFR, 'y', linewidth=0.5, label='low2')
    ax2.fill_between(x_IFR, IFR0, IFR_activation3_low3, facecolor='r')
    ax2.plot(x_IFR, low_IFR, 'r', linewidth=0.5, label='low3')
    ax2.set_title('Output membership (3 IFR low)')
    ax2.legend()

    for ax in (ax0, ax1, ax2):
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.get_xaxis().tick_bottom()
        ax.get_yaxis().tick_left()
    plt.tight_layout()

    # Aggregation & Defuzzification
    # Aggregate the first output membership functions together
    full_aggregated = np.fmax(IFR_activation2_moderate2,
                              np.fmax(IFR_activation2_maintain,
                                      np.fmax(IFR_activation2_maintain2,
                                              np.fmax(IFR_activation3_low,
                                                      np.fmax(IFR_activation3_low2,
                                                              np.fmax(IFR_activation3_low3,
                                                                      np.fmax(IFR_activation_vereyhigh,
                                                                              np.fmax(IFR_activation_high,
                                                                                      IFR_activation_moderate))))))))
    # print(len(full_aggregated))

    # Defuzzification
    output_IFR = fuzz.defuzz(x_IFR, full_aggregated, 'centroid')
    output_IFR_activation = fuzz.interp_membership(x_IFR, full_aggregated, output_IFR)  # for plot centro

    fig, ax0 = plt.subplots(figsize=(7, 9))
    ax0.plot(x_IFR, vereyhigh_IFR, 'b', linewidth=0.5, linestyle='--')
    ax0.plot(x_IFR, high_IFR, 'g', linewidth=0.5, linestyle='--')
    ax0.plot(x_IFR, modrate_IFR, 'c', linewidth=0.5, linestyle='--')
    ax0.plot(x_IFR, maintain_IFR, 'm', linewidth=0.5, linestyle='--')
    ax0.plot(x_IFR, low_IFR, 'k', linewidth=0.5, linestyle='--', )
    ax0.fill_between(x_IFR, IFR0, full_aggregated, facecolor='Pink', alpha=0.7)
    ax0.plot([output_IFR, output_IFR], [0, output_IFR_activation], 'k', linewidth=1.5, alpha=0.9, label="Centroid")
    ax0.set_title('Aggregated membership and result (line) for IFR very high, high, moderate & low.')
    ax0.legend(loc='upper right')

    for ax in (ax0, ax1, ax2):
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.get_xaxis().tick_bottom()
        ax.get_yaxis().tick_left()

    plt.tight_layout()

    Output_IFR = round(output_IFR)
    l3 = Label(fram, text=Output_IFR,font=("Akhbar MT",10,"bold"),bg="#81D4FA", width=12, height=1)
    l3.place(x=250, y=115)

    max_MAP = np.fmax(MAP_lo, np.fmax(MAP_norm, MAP_hi))
    max_HOU = np.fmax(HOU_lo, np.fmax(HOU_norm, HOU_hi))

    def thereason():
        if max_MAP == MAP_lo and max_HOU == HOU_lo:
            l6 = Label(fram,
                       text='The INTRAVENOUS FLUID RATE is very high\n      Because\nThe ARTERIAL BLOOD PRESSURE is low \nThe Hourly '
                            'Urine Output is low ', font=("Akhbar MT", 8, "bold"), bg="#FF4141", width=40, height=5)
            l6.place(x=250, y=230)
        elif max_MAP == MAP_lo and max_HOU == HOU_norm:
            l6 = Label(fram,
                       text='The INTRAVENOUS FLUID RATE is  high\n      Because\nThe ARTERIAL BLOOD PRESSURE is low \nThe Hourly Urine '
                            'Output is normal ', font=("Akhbar MT", 8, "bold"), bg="#F76767", width=40, height=5)
            l6.place(x=250, y=230)


        elif max_MAP == MAP_lo and max_HOU == HOU_hi:
            l6 = Label(fram,
                       text='The INTRAVENOUS FLUID RATE is moderate\n      Because\nThe ARTERIAL BLOOD PRESSURE is low \nThe '
                            'Hourly Urine Output is high ', font=("Akhbar MT", 8, "bold"), bg="#81D4FA", width=40, height=5)
            l6.place(x=250, y=230)


        elif max_MAP == MAP_norm and max_HOU == HOU_lo:
            l6 = Label(fram,
                       text='The INTRAVENOUS FLUID RATE is moderate\n      Because\nThe ARTERIAL BLOOD PRESSURE is normal \nThe '
                            'Hourly Urine Output is low ', font=("Akhbar MT", 8, "bold"), bg="#81D4FA", width=40, height=5)
            l6.place(x=250, y=230)

        elif max_MAP == MAP_norm and max_HOU == HOU_norm:
            l6 = Label(fram,
                       text='The INTRAVENOUS FLUID RATE is maintain\n      Because\nThe ARTERIAL BLOOD PRESSURE is normal \nThe '
                            'Hourly Urine Output is normal ', font=("Akhbar MT",8, "bold"), bg="#81D4FA", width=40, height=5)
            l6.place(x=250, y=230)

        elif max_MAP == MAP_norm and max_HOU == HOU_hi:
            l6 = Label(fram,
                       text='The INTRAVENOUS FLUID RATE is  maintain\n      Because\nThe ARTERIAL BLOOD PRESSURE is normal \nThe '
                            'Hourly Urine Output is high ', font=("Akhbar MT",8, "bold"), bg="#81D4FA", width=40, height=5)
            l6.place(x=250, y=230)

        elif max_MAP == MAP_hi and max_HOU == HOU_lo:
            l6 = Label(fram,
                       text='The INTRAVENOUS FLUID RATE is  low\n      Because\nThe ARTERIAL BLOOD PRESSURE is high \nThe Hourly '
                            'Urine Output is low ', font=("Akhbar MT",8, "bold"), bg="#81D4FA", width=40, height=5)
            l6.place(x=250, y=230)

        elif max_MAP == MAP_hi and max_HOU == HOU_norm:
            l6 = Label(fram,
                       text='The INTRAVENOUS FLUID RATE is  low\n      Because\nThe ARTERIAL BLOOD PRESSURE is high \nThe Hourly '
                            'Urine Output is normal ', font=("Akhbar MT",8, "bold"), bg="#81D4FA", width=40, height=5)
            l6.place(x=250, y=230)

        elif max_MAP == MAP_hi and max_HOU == HOU_hi:
            l6 = Label(fram,
                       text='The INTRAVENOUS FLUID RATE is  low\n      Because\nThe ARTERIAL BLOOD PRESSURE is high \nThe '
                            'Hourly '
                            'Urine Output is high ', font=("Akhbar MT",8, "bold"), bg="#81D4FA", width=40, height=5)
            l6.place(x=250, y=230)

    B3 = Button(fram, bg="#15EB21", text="Get reason", command=thereason)
    B3.place(x=380,y=170)




while True:
    def t():
        plt.show()

    B1 = Button(fram,bg="#15EB21", text="Get resulte", command=g)
    B1.place(x=250, y=170)
    B2=Button(fram,bg="#15EB21",text="plt.show",command=t)
    B2.place(x=320,y=170)

    fram.mainloop()
