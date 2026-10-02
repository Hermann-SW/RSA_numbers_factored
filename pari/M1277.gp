\\ M1277: https://factordb.com/index.php?query=M1277

n385=2601983048666099770481310081841021384653815561816676201329778087600902014918340074503059860433081046210605403488570251947845891562080866227034976651419330190731032377347305086443295837415395887618239855136922452802923419286887119716740625346109565072933087221327790207134604146257063901166556207972729700461767055550785130256674608872183239507219512717434046725178680177638925792182271;

p106=1724716499241899864602425389894492014760761058306262762892810886087012338823944627660237293943404138481321;

p117=174090709548829862673444876509956283267433847880436775401923086006338309086502338849028139248274886760517707263111447;

p163=8665849643335295674769105294571409283548491149467547745358388419546365219034102218289049713968532434665290528265538637566847289906584634645620272395224026405923633;

my_3prime_qfb(t) = {
    my([, n, p, q, r] = t);

    forstep(d = -3, -1000000, -1,
        my(D = if(d % 4 == 1 || d % 4 == 0, d, 4*d));
        if (!isfundamental(D), next);
        
        \\ Must split in all three primes
        if (kronecker(D, p) != 1 || kronecker(D, q) != 1 || kronecker(D, r) != 1, next);

        my(bp = Vec(qfbprimeform(D, p))[2]);
        my(bq = Vec(qfbprimeform(D, q))[2]);
        my(br = Vec(qfbprimeform(D, r))[2]);

        \\ The 4 distinct combinations modulo 2n (fixing +bp)
        my(signs = [[bp, bq, br], [bp, bq, -br], [bp, -bq, br], [bp, -bq, -br]]);
        my(res_list = List(), s_list = List());
        my(all_match = 1);

        for(i = 1, 4,
            my(b_p = signs[i][1], b_q = signs[i][2], b_r = signs[i][3]);
            my(B = lift(chinese(chinese(Mod(b_p, 2*p), Mod(b_q, 2*q)), Mod(b_r, 2*r))));
            if ((B^2 - D) % (4*n) != 0, B += 2*n);

            my(res = qfbredsl2(Qfb(n, B, (B^2 - D)/(4*n))));
            
            \\ Check if it reduces to (1, 0, z)
            my(Q = res[1]);
            if (Vec(Q)[1] != 1 || Vec(Q)[2] != 0, all_match = 0; break);

            if (i > 1 && res_list[1][1] != Q, all_match = 0; break);

            listput(res_list, res);
            my(M_inv = res[2]^-1);
            listput(s_list, Vec(M_inv[,1])~);
        );

        if (all_match && #s_list >= 3,
            \\ Ensure we have at least 3 distinct representations up to sign
            my(unique_s = List([s_list[1]]));
            for(k = 2, #s_list,
                my(is_new = 1);
                for(u = 1, #unique_s,
                    if (s_list[k] == unique_s[u] || s_list[k] == -unique_s[u],
                        is_new = 0; break;
                    );
                );
                if (is_new, listput(unique_s, s_list[k]));
            );

            if (#unique_s >= 3,
                return([D, res_list[1][1], unique_s[1], unique_s[2], unique_s[3]]);
            );
        );
    );
    error("No suitable discriminant found in search range");
}

extract_3prime_factors(sol, n) = {
    my(s1 = sol[3], s2 = sol[4], s3 = sol[5]);
    my(x1 = s1[1], y1 = s1[2]);
    my(x2 = s2[1], y2 = s2[2]);
    my(x3 = s3[1], y3 = s3[2]);

    my(terms = [
        abs(x1*y2 - x2*y1), x1*y2 + x2*y1,
        abs(x1*y3 - x3*y1), x1*y3 + x3*y1,
        abs(x2*y3 - x3*y2), x2*y3 + x3*y2
    ]);

    \\ Step 1: Collect non-trivial GCDs with N
    my(factors = List());
    for(k = 1, #terms,
        my(g = gcd(terms[k], n));
        if (g > 1 && g < n, listput(factors, g));
    );
    factors = Vec(factors);

    \\ Step 2: Pairwise GCDs to split composites
    my(prime_factors = List());
    for(k = 1, #factors,
        for(m = 1, #factors,
            my(g = gcd(factors[k], factors[m]));
            if (g > 1 && g < n, listput(prime_factors, g));
        );
    );
    prime_factors = Vec(Set(prime_factors));

    \\ Step 3: Filter out composite multiples
    my(primes = List());
    for(k = 1, #prime_factors,
        my(is_prime_factor = 1);
        my(fk = prime_factors[k]);
        for(m = 1, #prime_factors,
            if (k != m,
                my(fm = prime_factors[m]);
                if (fk % fm == 0, is_prime_factor = 0; break);
            );
        );
        if (is_prime_factor, listput(primes, fk));
    );
    
    return(Vec(primes));
}

sol = my_3prime_qfb([1277, n385, p106, p117, p163]);
print("discriminant=",sol[1]);
print("Qfb=",sol[2]);
print(qfeval(sol[2],sol[3])==n385);
print(qfeval(sol[2],sol[4])==n385);
print(qfeval(sol[2],sol[5])==n385);
print();

prms=extract_3prime_factors(sol,n385);
foreach(prms,p,print(#digits(p)," ",n385%p));

