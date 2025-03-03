# SSCP - Wind Tunnel CFD Comparisons

# Wind Tunnel CFD Comparisons

We are considering using the Sand Diego Wind Tunnel this cycle, which is logistically very good, but a bit smaller than Aerodyn.

[ Sand Diego Wind Tunnel](http://www.sandiegowindtunnel.com/)

[ Aerodyn](http://www.aerodynwindtunnel.com/tunnel-info)

These are CFD simulations are of Sundae-082 (our final aerobody) in differently-sized chambers.  Two of the chambers are modeled after the San Diego and Aerodyn tunnels.  All runs were performed with our usual speed (24.59m/s) and other typical settings.  Files are located in the Sundae Aero folder on FTP under wind_tunnel_sims/.

Results from Aerodyn and San Diego are relatively close to numbers from our typical "no-walls" CFD chamber.

## Run 1: Usual Tunnel

[](#h.oi5jn7rglm)

The standard tunnel used in our CFD simulations.  It's length and width are so big that the walls should have no effect.

drag: 27.99993N

lift: 1.345145N

![](../../../../../assets/image_afee359e3c.png)

![](../../../../../assets/image_e5ececd4ad.png)

## Run 2: "Aerodyn"

[](#h.acddqnt68vjh)

Tunnel modeled after the Aerodyn wind tunnel, has a cross-sectional area of 185ft^2.  This and all following tunnels had length 27.89ft.

drag: 30.46249N

lift: 0.6144074N

![](../../../../../assets/image_e2ab211ab2.png)

![](../../../../../assets/image_33fb18772b.png)

## Run 3: "San Diego"

[](#h.ytrjgakj4zbb)

Tunnel modeled after San Diego tunnel, has cross-sectional area of 95ft^2.  Tunnel length: 27.89ft.

drag: 31.76527N

lift: 2.017476N

![](../../../../../assets/image_f1975421b4.png)

![](../../../../../assets/image_84c638b582.png)

## Run 4: "Really Small Tunnel"

[](#h.b378cwdpa4ie)

Tunnel made to simulate really small wind tunnel, cross-sectional area of 19ft^2.  tunnel length: 27.89ft.

drag: 47.92374N

lift: 54.24022N (not converged)

![](../../../../../assets/image_7f7c634a3e.png)

![](../../../../../assets/image_89fb48a6e6.png)

